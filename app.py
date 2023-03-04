import streamlit as st
st.title('Giai phuong trinh bac 1')
a=st.number_input("tham so a")
b=st.number_input("tham so b")
if st.button("Giai"):
  if a==0 and b==0:
    st.success("Phuong trinh co vo so nghiem")
  elif a==0 and b!=0:
    st.success("Phuong trinh vo nghiem")
  else:
    result=-b/a
    st.success(f'Phuong trinh co 1 nghiem {result}')
