import streamlit as st

def calculate_bmr(weight, height, age, gender):
    if gender == "男性":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

def calculate_energy_requirements(bmr, stress_factor, activity_factor):
    energy_requirements = bmr * stress_factor * activity_factor
    return energy_requirements

st.title("エネルギー必要量計算")

weight = st.number_input("体重（kg）", min_value=0.0)
height = st.number_input("身長（cm）", min_value=0.0)
age = st.number_input("年齢", min_value=0, max_value=150)
gender = st.radio("性別", options=["男性", "女性"])

st.subheader("ストレス係数")
stress_factor_options = {"ストレスなし": 1.0, "手術": 1.2, "がん": 1.2}
stress_factor = st.selectbox("ストレス係数", list(stress_factor_options.keys()))

st.subheader("活動係数")
activity_factor_options = {"寝たきり": 1.0, "ベッド上安静": 1.2, "ベッド以外での活動あり": 1.3, "軽労作": 1.5}
activity_factor = st.selectbox("活動係数", list(activity_factor_options.keys()))

if st.button("計算"):
    bmr = calculate_bmr(weight, height, age, gender)
    stress_factor_value = stress_factor_options[stress_factor]
    activity_factor_value = activity_factor_options[activity_factor]
    energy_requirements = calculate_energy_requirements(bmr, stress_factor_value, activity_factor_value)
    st.success(f"あなたの基礎代謝量は {bmr:.2f} kcalです。")
    st.success(f"あなたのエネルギー必要量は {energy_requirements:.2f} kcalです。")
