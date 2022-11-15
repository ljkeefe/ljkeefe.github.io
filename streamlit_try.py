import streamlit as st
import pandas as pd

df1 = pd.DataFrame([['Item 1',2,3.1], ['Item 2',5,6.1], ['Item 3',8,9.1]], columns = ['col1', 'col2', 'col3']).sort_values('col3', ascending=False).set_index('col1')
df2 = pd.DataFrame([['Item 1',2,4.1], ['Item 2',5,10.1], ['Item 3',8,9.1]], columns = ['col1', 'col2', 'col3']).sort_values('col3', ascending=False).set_index('col1')

st.markdown('<center><p style="color:green; font-size:40px; font-weight: bold;">Mock-up Dashboard</p></center>',unsafe_allow_html=True)
st.header('Uncontrained TURF')

default_vals = None

col1, col2 = st.columns((1,1))

with col1:
    st.markdown('<center>T1B</center>',unsafe_allow_html=True)
    t1b_unconstRows = st.multiselect(
    "Choose Concepts", list(df1.index), key = 0, default = list(df1.index)
)
    if not t1b_unconstRows:
        st.error("Please select at least one country.")
    else:
        data = df1.loc[t1b_unconstRows]
        st.table(data = data)
        aggy = 0
        for i in data.index:
            aggy = aggy + data.loc[i, 'col3']
        st.metric(label="Cumulative Reach", value=(str(round(aggy,2)) + '%'))
        st.bar_chart(data=data, x='col2', y='col3')
        
with col2:
    st.markdown('<center>T2B</center>',unsafe_allow_html=True)
    t2b_unconstRows = st.multiselect(
    "Choose Concepts", list(df2.index), key = 1, default = list(df2.index)
)
    if not t2b_unconstRows:
        st.error("Please select at least one country.")
    else:
        data2 = df2.loc[t2b_unconstRows]
        st.table(data = data2)
        aggy = 0
        for i in data2.index:
            aggy = aggy + data2.loc[i, 'col3']
        st.metric(label="Cumulative Reach", value=(str(aggy) + '%'))
        st.bar_chart(data=data, x='col2', y='col3')
        
st.header('Contrained TURF')
st.markdown('<p style="font-size: 25px;"><i>Concepts Constrained: 1, 2</i></p>',unsafe_allow_html=True)

juice = ['Item 1','Item 2']
df1_const_list = list(filter(lambda x: x not in juice, list(df1.index)))
df2_const_list = list(filter(lambda x: x not in juice, list(df2.index)))


col3, col4 = st.columns((1,1))

with col3:
    st.markdown('<center>T1B</center>',unsafe_allow_html=True)
    t1b_constRows = st.multiselect(
    "Choose Concepts", df1_const_list, key = 2, default = df1_const_list
)
    if not t1b_constRows:
        data = df1.loc[juice]
        st.table(data = data)
        aggy = 0
        for i in data.index:
            aggy = aggy + data.loc[i, 'col3']
        st.metric(label="Cumulative Reach", value=(str(aggy) + '%'))
    else:
        df1_list = juice + t1b_constRows
        data = df1.loc[df1_list]
        st.table(data = data)
        aggy = 0
        for i in data.index:
            aggy = aggy + data.loc[i, 'col3']
        st.metric(label="Cumulative Reach", value=(str(aggy) + '%'))
        
with col4:
    st.markdown('<center>T2B</center>',unsafe_allow_html=True)
    t2b_constRows = st.multiselect(
    "Choose Concepts", df2_const_list, key = 3, default = df2_const_list
)
    if not t2b_constRows:
        data2 = df2.loc[juice]
        st.table(data = data2)
        aggy = 0
        for i in data2.index:
            aggy = aggy + data2.loc[i, 'col3']
        st.metric(label="Cumulative Reach", value=(str(aggy) + '%'))
    else:
        df2_list = juice + t2b_constRows
        data2 = df2.loc[df2_list]
        st.table(data = data2)
        aggy = 0
        for i in data2.index:
            aggy = aggy + data2.loc[i, 'col3']
        st.metric(label="Cumulative Reach", value=(str(aggy) + '%'))
        

md_tbl = pd.DataFrame([['Nikes', 45, 'Item 1'],['Reebok', 25, 'Item 2'], ['Addidas', 20, 'Item 3']], columns = ['Concept', 'MaxDiff Score', 'Concept #'])  
st.header('MaxDiff')

def active_row_style(row):
    global cutoff
    if row['MaxDiff Score'] >= cutoff:
        return pd.Series('background-color: lightgreen', row.index)
    else:
        return pd.Series('', row.index)

cutoff = st.number_input(label='Share of Preference (MaxDiff Score) Cutoff Point', step = 1)
st.table(data = md_tbl.style.apply(active_row_style, axis = 1))

anchor_md_tbl = pd.DataFrame([['Nikes', 230, 45, 'Item 1'],['Reebok', 125, 25, 'Item 2'], ['Addidas', 99, 20, 'Item 3']], columns = ['Concept', 'Anchored Score', 'MaxDiff Score', 'Concept #'])  
st.header('Anchored MaxDiff')


def row_style(row):
    if row['Anchored Score'] >= 100:
        return pd.Series('background-color: lightgreen;', row.index)
    else:
        return pd.Series('', row.index)

st.table(data = anchor_md_tbl.style.apply(row_style, axis = 1))