import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi

def calculate_bmr(weight, height, age, gender):
    if gender == "男性":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        formula = "BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)"
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        formula = "BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)"
    return bmr, formula

def calculate_energy_requirements(bmr, stress_factor, activity_factor):
    energy_requirements = bmr * stress_factor * activity_factor
    return energy_requirements

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "やせ"
    elif 18.5 <= bmi < 25:
        return "ふつう"
    else:
        return "肥満"

st.title("エネルギー必要量計算")

weight = st.slider("体重（kg）", min_value=30, max_value=130, step=1, value=60)
height = st.slider("身長（cm）", min_value=100, max_value=200, step=1, value=160)
age = st.slider("年齢", min_value=10, max_value=100, step=1, value=30)
gender = st.radio("性別", options=["男性", "女性"], index=0)

st.subheader("計算式")
if gender == "男性":
    st.text("BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)")
else:
    st.text("BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)")

st.subheader("ストレス係数と活動係数")
stress_factor_options = {"ストレスなし (1.0)": 1.0, "手術 (1.2)": 1.2, "がん (1.2)": 1.2}
stress_factor = st.radio("ストレス係数", options=list(stress_factor_options.keys()), index=0)

activity_factor_options = {"寝たきり (1.0)": 1.0, "ベッド上安静 (1.2)": 1.2, "ベッド以外での活動あり (1.3)": 1.3, "軽労作 (1.5)": 1.5}
activity_factor = st.radio("活動係数", options=list(activity_factor_options.keys()), index=0)

if st.button("計算"):
    bmi = calculate_bmi(weight, height)
    bmr, formula = calculate_bmr(weight, height, age, gender)
    stress_factor_value = stress_factor_options[stress_factor]
    activity_factor_value = activity_factor_options[activity_factor]
    energy_requirements = calculate_energy_requirements(bmr, stress_factor_value, activity_factor_value)
    bmi_interpretation = interpret_bmi(bmi)
    st.success(f"あなたのBMIは {bmi:.2f} で、体型は「{bmi_interpretation}」です。")
    st.success(f"あなたの基礎代謝量は {bmr:.2f} kcalです。")
    st.success(f"あなたのエネルギー必要量は {energy_requirements:.2f} kcalです。")
