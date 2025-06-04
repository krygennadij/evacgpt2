import streamlit as st
import pandas as pd
import numpy as np

# Настройки страницы
st.set_page_config(
    page_title="ЭвакGPT",
    page_icon="🔥",
    layout="wide"
)

# Стили CSS для оформления
st.markdown("""
<style>
    .header {
        font-size: 24px;
        font-weight: bold;
        color: #FF4B4B;
        margin-bottom: 10px;
    }
    .subheader {
        font-size: 18px;
        font-weight: bold;
        color: #FF4B4B;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .warning {
        background-color: #FFF3CD;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #FFC107;
        margin: 10px 0;
    }
    .danger {
        background-color: #F8D7DA;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #DC3545;
        margin: 10px 0;
    }
    .info-box {
        border: 1px solid #D3D3D3;
        border-radius: 5px;
        padding: 15px;
        margin: 10px 0;
    }
    .divider {
        border-top: 2px dashed #D3D3D3;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- ВИЗУАЛЬНОЕ ОФОРМЛЕНИЕ ПОД МАКЕТ ---

# Крупная шапка с иконкой и цветом
st.markdown(
    '''<div style="display: flex; align-items: center; gap: 20px; margin-bottom: 0;">
        <span style="font-size: 48px;">🔥</span>
        <span style="font-size: 38px; font-weight: bold; color: #FF4B4B; letter-spacing: 2px;">ЭвакGPT</span>
    </div>''',
    unsafe_allow_html=True
)

st.markdown('<div style="font-size: 20px; color: #444; margin-bottom: 30px;">Интеллектуальная система мониторинга и оценки уровня пожарной опасности</div>', unsafe_allow_html=True)

# --- ОСНОВНОЙ КОНТЕНТ ---

st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

st.markdown('<div style="font-size: 28px; font-weight: bold; color: #222; margin-bottom: 20px;">Результаты оценки</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Параметры объекта")

    object_address = st.text_input("Адрес объекта:")
    building_purpose = st.selectbox(
        "Класс функциональной пожарной опасности:", 
        [
            "Выберите класс",
            "Ф1.1 - здания дошкольных образовательных организаций",
            "Ф1.1 - спальные корпуса образовательных организаций с наличием интерната и детских организаций",
            "Ф1.1 - специализированные дома для престарелых",
            "Ф1.1 - специализированные дома инвалидов",
            "Ф1.1 - больницы",
            "Ф1.2 - гостиницы, общежития (за исключением общежитий квартирного типа), спальные корпуса санаториев и домов отдыха общего типа, кемпингов",
            "Ф1.3 - многоквартирные жилые дома, в том числе общежития квартирного типа",
            "Ф1.4 - одноквартирные жилые дома, в том числе блокированные",
            "Ф2.1, Ф2.3 - детские театры, цирки",
            "Ф2.1, Ф2.3 - театры, кинотеатры, концертные залы, клубы, цирки, спортивные сооружения с трибунами",
            "Ф2.1, Ф2.3 - библиотеки",
            "Ф2.2, Ф2.4 - танцевальные залы",
            "Ф2.2, Ф2.4 - музеи, выставки",
            "Ф3.1 - здания организаций торговли",
            "Ф3.2 - здания организаций общественного питания",
            "Ф3.3 - вокзалы",
            "Ф3.4 - здания медицинских организаций (поликлиники, амбулатории и т.д.) для вхрослых людей",
            "Ф3.4 - здания медицинских организаций (поликлиники, амбулатории и т.д.) для детей и подростков",
            "Ф3.5 - организации бытового и коммунального обслуживания",
            "Ф3.6 - физкультурно-оздоровительные и спортивно-тренировочные учреждения для детей",
            "Ф3.6 - физкультурно-оздоровительные и спортивно-тренировочные учреждения (для взрослых) с помещениями без трибун для зрителей, бытовые помещения, бани",
            "Ф3.7 - здания православного культового назначения",
            "Ф4.1 - здания общеобразовательных организаций, организаций дополнительного образования детей и подростков",
            "Ф4.2 - здания образовательных организаций высшего образования, организаций дополнительного профессионального образования",
            "Ф4.3 - административные здания, здания проектно-конструкторских организаций, информационных и редакционно-издательских организаций, научных организаций, банков, контор, офисов",
            "Ф4.4 - здания пожарных депо",
            "Ф5.1 - производственные здания, сооружения, производственные и лабораторные помещения, мастерские, крематории",
            "Ф5.2 - складские здания, сооружения, книгохранилища, архивы",
            "Ф5.2 - отдельностоящее здание стоянки для автомобилей без технического обслуживания и ремонта",
        ]
    )
    building_floors = st.number_input("Этажность здания:", min_value=1, step=1)

    automation_state = st.radio(
        "Состояние противопожарной автоматики:",
        ["системы своевременно обслуживаются", "системы не обслуживаются"]
    )

    evacuation_routes_state = st.radio(
        "Состояние эвакуационных путей и выходов:",
        ["загромождены", "не загромождены"]
    )

    training_state = st.radio(
        "Проведение учебных эвакуаций и обучения действиям при пожаре:",
        ["Проводятся согласно плану", "Проводятся редко, не проводятся"]
    )

# Справочник базовых времен для классов 
BASE_EVAC_TIME = {
    "Ф1.1 - здания дошкольных образовательных организаций": 4.0,
    "Ф1.1 - спальные корпуса образовательных организаций с наличием интерната и детских организаций": 4.0,
    "Ф1.1 - специализированные дома для престарелых": 4.0,
    "Ф1.1 - специализированные дома инвалидов": 4.0,
    "Ф1.1 - больницы": 4.0,
    "Ф1.2 - гостиницы, общежития (за исключением общежитий квартирного типа), спальные корпуса санаториев и домов отдыха общего типа, кемпингов": 9.0,
    "Ф1.3 - многоквартирные жилые дома, в том числе общежития квартирного типа": 9.0,
    "Ф1.4 - одноквартирные жилые дома, в том числе блокированные": 9.0,
    "Ф2.1, Ф2.3 - детские театры, цирки": 3.5,
    "Ф2.1, Ф2.3 - театры, кинотеатры, концертные залы, клубы, цирки, спортивные сооружения с трибунами": 3.5,
    "Ф2.1, Ф2.3 - библиотеки": 3.5,
    "Ф2.2, Ф2.4 - танцевальные залы": 3.5,
    "Ф2.2, Ф2.4 - музеи, выставки": 3.5,
    "Ф3.1 - здания организаций торговли": 3.5,
    "Ф3.2 - здания организаций общественного питания": 3.5,
    "Ф3.3 - вокзалы": 3.5,
    "Ф3.4 - здания медицинских организаций (поликлиники, амбулатории и т.д.) для вхрослых людей": 3.5,
    "Ф3.4 - здания медицинских организаций (поликлиники, амбулатории и т.д.) для детей и подростков": 6.0,
    "Ф3.5 - организации бытового и коммунального обслуживания": 3.5,
    "Ф3.6 - физкультурно-оздоровительные и спортивно-тренировочные учреждения для детей": 6.0,
    "Ф3.6 - физкультурно-оздоровительные и спортивно-тренировочные учреждения (для взрослых) с помещениями без трибун для зрителей, бытовые помещения, бани": 6.0,
    "Ф3.7 - здания православного культового назначения": 3.5,
    "Ф4.1 - здания общеобразовательных организаций, организаций дополнительного образования детей и подростков": 6.0,
    "Ф4.2 - здания образовательных организаций высшего образования, организаций дополнительного профессионального образования": 6.0,
    "Ф4.3 - административные здания, здания проектно-конструкторских организаций, информационных и редакционно-издательских организаций, научных организаций, банков, контор, офисов": 6.0,
    "Ф4.4 - здания пожарных депо": 3.5,
    "Ф5.1 - производственные здания, сооружения, производственные и лабораторные помещения, мастерские, крематории": 6.0,
    "Ф5.2 - складские здания, сооружения, книгохранилища, архивы": 6.0,
    "Ф5.2 - отдельностоящее здание стоянки для автомобилей без технического обслуживания и ремонта": 3.5,
}

def apply_floor_correction(base_time, floors):
    if base_time < 5:
        return base_time + 0.5
    elif 5 <= base_time < 10:
        return base_time + 1.5
    elif 10 <= base_time < 15:
        return base_time + 2.5
    elif 15 <= base_time < 20:
        return base_time + 3.5
    elif 20 <= base_time < 25:
        return base_time + 4.5
    elif 25 <= base_time < 30:
        return base_time + 5.5
    else:
        return "Уточните исходные данные"

def calculate_standard_evacuation_time(building_type, floors, linked_type=None):
    # 1. Считаем базовое время по классу
    if building_type == "Ф1.1 - здания дошкольных образовательных организаций":
        base = 4 + 0.55 + (floors - 1) * 0.61
    elif building_type == "Ф1.1 - спальные корпуса образовательных организаций с наличием интерната и детских организаций":
        base = 4 + 1.58 + (floors - 1) * 0.45
    elif building_type == "Ф1.1 - специализированные дома для престарелых":
        base = 4 + 2.58 + (floors - 1) * 1.13
    elif building_type == "Ф1.1 - специализированные дома инвалидов":
        base = 4 + 2.44 + (floors - 1) * 0.89
    elif building_type == "Ф1.1 - больницы":
        base = 4 + 2.44 + (floors - 1) * 0.89
    elif building_type == "Ф1.2 - гостиницы, общежития (за исключением общежитий квартирного типа), спальные корпуса санаториев и домов отдыха общего типа, кемпингов":
        base = 9 + 1.33 + (floors - 1) * 0.26
    elif building_type == "Ф1.3 - многоквартирные жилые дома, в том числе общежития квартирного типа":
        base = 9 + 0.59 + (floors - 1) * 0.4
    elif building_type == "Ф1.4 - одноквартирные жилые дома, в том числе блокированные":
        base = 9 + 0.59
    elif building_type == "Ф2.1, Ф2.3 - детские театры, цирки":
        base = 3.5 + 3.12 + (floors - 1) * 1.58
    elif building_type == "Ф2.1, Ф2.3 - театры, кинотеатры, концертные залы, клубы, цирки, спортивные сооружения с трибунами":
        base = 3.5 + 3.34 + (floors - 1) * 1.82
    elif building_type == "Ф2.1, Ф2.3 - библиотеки":
        base = 3.5 + 1.06 + (floors - 1) * 0.24
    elif building_type == "Ф2.2, Ф2.4 - танцевальные залы":
        base = 3.5 + 2.65 + (floors - 1) * 1.03
    elif building_type == "Ф2.2, Ф2.4 - музеи, выставки":
        base = 3.5 + 3.34 + (floors - 1) * 1.82
    elif building_type == "Ф3.1 - здания организаций торговли":
        base = 3.5 + 3.34 + (floors - 1) * 1.82
    elif building_type == "Ф3.2 - здания организаций общественного питания":
        base = 3.5 + 3.34 + (floors - 1) * 1.82
    elif building_type == "Ф3.3 - вокзалы":
        base = 3.5 + 3.34 + (floors - 1) * 1.82
    elif building_type == "Ф3.4 - здания медицинских организаций (поликлиники, амбулатории и т.д.) для вхрослых людей":
        base = 3.5 + 1.59 + (floors - 1) * 0.42
    elif building_type == "Ф3.4 - здания медицинских организаций (поликлиники, амбулатории и т.д.) для детей и подростков":
        base = 6 + 1.7 + (floors - 1) * 0.49
    elif building_type == "Ф3.5 - организации бытового и коммунального обслуживания":
        base = 3.5 + 1.77 + (floors - 1) * 0.55
    elif building_type == "Ф3.6 - физкультурно-оздоровительные и спортивно-тренировочные учреждения для детей":
        base = 6 + 3.12 + (floors - 1) * 1.58
    elif building_type == "Ф3.6 - физкультурно-оздоровительные и спортивно-тренировочные учреждения (для взрослых) с помещениями без трибун для зрителей, бытовые помещения, бани":
        base = 6 + 2.87 + (floors - 1) * 1.34
    elif building_type == "Ф3.7 - здания православного культового назначения":
        base = 3.5 + 5.29 + (floors - 1) * 2
    elif building_type == "Ф4.1 - здания общеобразовательных организаций, организаций дополнительного образования детей и подростков":
        base = 6 + 1.58 + (floors - 1) * 0.45
    elif building_type == "Ф4.2 - здания образовательных организаций высшего образования, организаций дополнительного профессионального образования":
        base = 6 + 1.53 + (floors - 1) * 0.3
    elif building_type == "Ф4.3 - административные здания, здания проектно-конструкторских организаций, информационных и редакционно-издательских организаций, научных организаций, банков, контор, офисов":
        base = 6 + 1.53 + (floors - 1) * 0.32
    elif building_type == "Ф4.4 - здания пожарных депо":
        base = 3.5 + 1.06 + (floors - 1) * 0.32
    elif building_type == "Ф5.1 - производственные здания, сооружения, производственные и лабораторные помещения, мастерские, крематории":
        base = 6 + 1.01 + (floors - 1) * 0.19
    elif building_type == "Ф5.2 - складские здания, сооружения, книгохранилища, архивы":
        base = 6 + 1.01 + (floors - 1) * 0.19
    elif building_type == "Ф5.2 - отдельностоящее здание стоянки для автомобилей без технического обслуживания и ремонта":
        base = 3.5 + 3.34 + (floors - 1) * 0.19
    elif building_type == "Ф5.2 - стоянка для автомобилей без технического обслуживания и ремонта, относящаяся к объекту другого функционального назначения":
        if linked_type == "Ф1.2 - гостиницы, общежития (за исключением общежитий квартирного типа), спальные корпуса санаториев и домов отдыха общего типа, кемпингов":
            base = 3.5 + 3.34 + (floors - 1) * 0.26
        elif linked_type == "Ф1.3 - многоквартирные жилые дома, в том числе общежития квартирного типа":
            base = 3.5 + 5.29 + (floors - 1) * 0.4
        elif linked_type == "Ф2.1, Ф2.3 - театры, кинотеатры, концертные залы, клубы, цирки, спортивные сооружения с трибунами":
            base = 3.5 + 1.33 + (floors - 1) * 1.82
        elif linked_type == "Ф3.1 - здания организаций торговли":
            base = 3.5 + 3.34 + (floors - 1) * 1.82
        elif linked_type == "Ф3.2 - здания организаций общественного питания":
            base = 3.5 + 3.34 + (floors - 1) * 1.82
        elif linked_type == "Ф3.6 - физкультурно-оздоровительные и спортивно-тренировочные учреждения (для взрослых) с помещениями без трибун для зрителей, бытовые помещения, бани":
            base = 3.5 + 2.87 + (floors - 1) * 1.34
        elif linked_type == "Ф4.3 - административные здания, здания проектно-конструкторских организаций, информационных и редакционно-издательских организаций, научных организаций, банков, контор, офисов":
            base = 3.5 + 1.53 + (floors - 1) * 0.32
        elif linked_type == "Ф5.1 - производственные здания, сооружения, производственные и лабораторные помещения, мастерские, крематории":
            base = 3.5 + 1.01 + (floors - 1) * 0.32
        else:
            return "Уточните исходные данные"
    else:
        return "Уточните исходные данные"
    
    # 2. Корректировка по диапазону этажности
    return apply_floor_correction(base, floors)

# Функция для расчета прогнозируемого времени эвакуации
def calculate_predicted_evacuation_time(standard_time, automation_status, evacuation_status, training_status):
    # Базовое время зависит от состояния автоматики
    if automation_status == "системы своевременно обслуживаются":
        predicted_time = standard_time
    else:
        predicted_time = standard_time * 1.25
    
    # Добавляем время за загромождённые пути
    if evacuation_status == "загромождены":
        predicted_time += standard_time * 0.25
    
    # Добавляем время за отсутствие тренировок
    if training_status == "Проводятся редко, не проводятся":
        predicted_time += standard_time * 0.25
    
    return predicted_time

# Функция для определения уровня опасности
def determine_danger_level(standard_time, predicted_time):
    ratio = predicted_time / standard_time
    
    if ratio == 1:
        return "Допустимый"
    elif ratio <= 1.25:
        return "Повышенный"
    elif ratio <= 1.5:
        return "Высокий"
    elif ratio <= 1.75:
        return "Критический"
    else:
        return "Уточните исходные данные"

# Функция для определения рекомендуемых действий
def determine_recommended_actions(automation_status, evacuation_status, training_status, danger_level):
    if (automation_status == "системы своевременно обслуживаются" and 
        evacuation_status == "не загромождены" and 
        training_status == "Проводятся согласно плану"):
        return "Продолжить правильную эксплуатацию объекта защиты"
    
    elif (automation_status == "системы не обслуживаются" and 
          evacuation_status == "не загромождены" and 
          training_status == "Проводятся согласно плану"):
        return "Обеспечить плановое обслуживание систем противопожарной защиты"
    
    elif (automation_status == "системы своевременно обслуживаются" and 
          evacuation_status == "загромождены" and 
          training_status == "Проводятся согласно плану"):
        return "Обеспечить беспрепятственное движение людей по путям эвакуации и через эвакуационные выходы"
    
    elif (automation_status == "системы своевременно обслуживаются" and 
          evacuation_status == "не загромождены" and 
          training_status == "Проводятся редко, не проводятся"):
        return "Обеспечить проведение плановых тренировок по эвакуации и обучение действиям при пожаре"
    
    elif (automation_status == "системы не обслуживаются" and 
          evacuation_status == "загромождены" and 
          training_status == "Проводятся согласно плану"):
        return "1) Обеспечить плановое обслуживание систем противопожарной защиты; 2) Обеспечить беспрепятственное движение людей по путям эвакуации и через эвакуационные выходы"
    
    elif (automation_status == "системы не обслуживаются" and 
          evacuation_status == "не загромождены" and 
          training_status == "Проводятся редко, не проводятся"):
        return "1) Обеспечить плановое обслуживание систем противопожарной защиты; 2) Обеспечить проведение плановых тренировок по эвакуации и обучение действиям при пожаре"
    
    elif (automation_status == "системы своевременно обслуживаются" and 
          evacuation_status == "загромождены" and 
          training_status == "Проводятся редко, не проводятся"):
        return "1) Обеспечить беспрепятственное движение людей по путям эвакуации и через эвакуационные выходы; 2) Обеспечить проведение плановых тренировок по эвакуации и обучение действиям при пожаре"
    
    elif (automation_status == "системы не обслуживаются" and 
          evacuation_status == "загромождены" and 
          training_status == "Проводятся редко, не проводятся"):
        return "1) Обеспечить плановое обслуживание систем противопожарной защиты; 2) Обеспечить беспрепятственное движение людей по путям эвакуации и через эвакуационные выходы; 3) Обеспечить проведение плановых тренировок по эвакуации и обучение действиям при пожаре"
    
    else:
        return "Уточните исходные данные"

# Main content area

# Проверяем, что все необходимые данные введены
if building_purpose != "Выберите класс" and building_floors > 0:
    # Рассчитываем эталонное время эвакуации
    standard_time = calculate_standard_evacuation_time(building_purpose, building_floors)
    
    # Рассчитываем прогнозируемое время эвакуации
    predicted_time = calculate_predicted_evacuation_time(
        standard_time,
        automation_state,
        evacuation_routes_state,
        training_state
    )
    
    # Определяем уровень опасности
    danger_level = determine_danger_level(standard_time, predicted_time)
    
    # Определяем рекомендуемые действия
    recommended_actions = determine_recommended_actions(
        automation_state,
        evacuation_routes_state,
        training_state,
        danger_level
    )
    
    # Цвета для уровней
    danger_colors = {
        "Допустимый": "#4CAF50",
        "Повышенный": "#FFC107",
        "Высокий": "#FF5722",
        "Критический": "#D32F2F",
        "Уточните исходные данные": "#757575"
    }
    color = danger_colors.get(danger_level, "#757575")

    # Блок с результатами
    st.markdown(f'''
    <div style="display: flex; gap: 32px; margin-bottom: 32px;">
        <div style="flex:1; background: #f7f7f7; border-radius: 18px; padding: 32px 24px; box-shadow: 0 2px 8px #0001;">
            <div style="font-size: 18px; color: #888;">Эталонное время эвакуации</div>
            <div style="font-size: 36px; font-weight: bold; color: #222;">{standard_time:.2f} мин</div>
        </div>
        <div style="flex:1; background: #f7f7f7; border-radius: 18px; padding: 32px 24px; box-shadow: 0 2px 8px #0001;">
            <div style="font-size: 18px; color: #888;">Прогнозируемое время эвакуации</div>
            <div style="font-size: 36px; font-weight: bold; color: #222;">{predicted_time:.2f} мин</div>
        </div>
        <div style="flex:1; background: {color}22; border-radius: 18px; padding: 32px 24px; box-shadow: 0 2px 8px #0001; border: 2px solid {color};">
            <div style="font-size: 18px; color: #888;">Уровень пожарной опасности</div>
            <div style="font-size: 32px; font-weight: bold; color: {color};">{danger_level}</div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Блок с рекомендациями
    # Форматируем рекомендации для красивого отображения
    if ";" in recommended_actions:
        actions_list = recommended_actions.split("; ")
        formatted_actions = ""
        for i, action in enumerate(actions_list):
            action_text = action.strip()
            if action_text.startswith(f"{i+1})"):
                action_text = action_text[3:].strip()
            formatted_actions += f'<div style="display: flex; align-items: flex-start; margin-bottom: 12px;"><span style="font-size: 20px; margin-right: 12px; color: #FF9800;">⚠️</span><span style="font-size: 17px; color: #333; line-height: 1.5;">{action_text}</span></div>'
        st.markdown(
            f'<div style="background: #fffbe6; border-left: 8px solid #FFB300; border-radius: 12px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 2px 8px #0001;">'
            f'<div style="font-size: 22px; font-weight: bold; color: #FF9800; margin-bottom: 16px;"><span style="font-size: 24px; margin-right: 8px;">⚡</span>Рекомендуемые действия</div>'
            f'{formatted_actions}'
            f'</div>',
            unsafe_allow_html=True
        )
    else:
        icon = "✅" if "Продолжить правильную эксплуатацию" in recommended_actions else "⚠️"
        bg_color = "#e8f5e9" if "Продолжить правильную эксплуатацию" in recommended_actions else "#fffbe6"
        border_color = "#4CAF50" if "Продолжить правильную эксплуатацию" in recommended_actions else "#FFB300"
        title_color = "#2E7D32" if "Продолжить правильную эксплуатацию" in recommended_actions else "#FF9800"
        st.markdown(
            f'<div style="background: {bg_color}; border-left: 8px solid {border_color}; border-radius: 12px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 2px 8px #0001;">'
            f'<div style="font-size: 22px; font-weight: bold; color: {title_color}; margin-bottom: 12px;"><span style="font-size: 24px; margin-right: 8px;">{icon}</span>Рекомендуемые действия</div>'
            f'<div style="font-size: 18px; color: #333; line-height: 1.5;">{recommended_actions}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

else:
    st.markdown('<div style="color:#D32F2F; font-size:20px; margin-top:40px;">Пожалуйста, заполните все необходимые поля в сайдбаре для получения результатов.</div>', unsafe_allow_html=True)