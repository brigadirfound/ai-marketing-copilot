import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import math

# Настройка страницы
st.set_page_config(
    page_title="AI Маркетинг Помощник",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Кастомный CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 2rem;
        text-align: center;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .insight-box {
        background: #f8fafc;
        border-left: 4px solid #10b981;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    .competitor-card {
        border: 1px solid #e5e7eb;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        background: white;
    }
    .price-card {
        border: 1px solid #d1d5db;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        background: #f9fafb;
    }
    .calculator-result {
        background: #ecfdf5;
        border: 2px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    .headline-variant {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .trend-item {
        background: #fef3c7;
        border-left: 4px solid #f59e0b;
        padding: 0.8rem;
        margin: 0.5rem 0;
        border-radius: 0 6px 6px 0;
    }
</style>
""", unsafe_allow_html=True)

# Заголовок
st.markdown('<h1 class="main-header">🎯 AI Маркетинг Помощник для Онлайн Школ</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #6b7280; font-size: 1.2rem;">Анализ конкурентов • Генерация креативов • Расчет юнит-экономики</p>', unsafe_allow_html=True)

# Боковая панель
with st.sidebar:
    st.header("🔧 Настройки")
    
    # Конфигурация API
    with st.expander("🔑 API Ключи"):
        fb_token = st.text_input("Facebook Access Token", type="password")
        google_token = st.text_input("Google Ads Token", type="password")
        vk_token = st.text_input("VK Ads Token", type="password")
    
    # Фильтры
    st.header("📊 Фильтры")
    niche_filter = st.selectbox(
        "Ниша",
        ["Все ниши", "Цифровой маркетинг", "Программирование", "Дизайн", "Бизнес", "Языки"]
    )

# Основные метрики
col1, col2, col3, col4 = st.columns(4)

sample_metrics = {
    "Цена лида": {"value": "1,250₽", "change": -15},
    "ROAS": {"value": "320%", "change": 8}, 
    "CTR": {"value": "2.4%", "change": -5},
    "Конверсия": {"value": "3.2%", "change": 12}
}

for i, (metric, data) in enumerate(sample_metrics.items()):
    with [col1, col2, col3, col4][i]:
        delta_color = "normal" if data["change"] > 0 else "inverse"
        st.metric(
            label=metric,
            value=data["value"],
            delta=f"{data['change']:+}%",
            delta_color=delta_color
        )

st.divider()

# Основные вкладки
tab1, tab2, tab3 = st.tabs(["🕵️ Анализ конкурентов", "🎨 Генератор креативов", "💰 Калькулятор юнит-экономики"])

with tab1:
    st.header("🕵️ Анализ конкурентов")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🔍 Анализ конкурента")
        competitor_url = st.text_input(
            "URL конкурента или страница в соцсетях",
            placeholder="https://example.com или @конкурент"
        )
        
        if st.button("🔍 Анализировать", type="primary"):
            with st.spinner("Анализируем конкурента..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    progress_bar.progress(i + 1)
                
                st.success("✅ Анализ завершен!")
                
                # Основные данные
                col_info1, col_info2 = st.columns(2)
                
                with col_info1:
                    st.markdown("""
                    **📊 Реклама и трафик:**
                    - Рекламный бюджет: ~450,000₽/месяц
                    - Активных кампаний: 18
                    - Основная площадка: Facebook (60%)
                    - Средний CPC: 28₽
                    """)
                
                with col_info2:
                    st.markdown("""
                    **🎯 Стратегия:**
                    - Главное предложение: "За 3 месяца к результату"
                    - Оценка лендинга: 8.7/10
                    - Основная аудитория: 25-35 лет
                    - Динамика: рост активности +40%
                    """)
        
        # Анализ цен конкурентов
        st.subheader("💰 Анализ цен в нише")
        
        if st.button("📊 Проанализировать цены"):
            with st.spinner("Собираем данные по ценам..."):
                # Мок-данные по ценам
                price_data = [
                    {"name": "Конкурент А", "price": "29,900₽", "type": "Базовый курс", "duration": "2 месяца"},
                    {"name": "Конкурент Б", "price": "49,900₽", "type": "Премиум", "duration": "4 месяца"},
                    {"name": "Конкурент В", "price": "19,900₽", "type": "Мини-курс", "duration": "1 месяц"},
                    {"name": "Конкурент Г", "price": "79,900₽", "type": "VIP", "duration": "6 месяцев"},
                    {"name": "Ваш курс", "price": "39,900₽", "type": "Стандарт", "duration": "3 месяца"}
                ]
                
                st.success("✅ Данные по ценам собраны!")
                
                for competitor in price_data:
                    color = "#e3f2fd" if competitor["name"] == "Ваш курс" else "#f9fafb"
                    st.markdown(f"""
                    <div style="background: {color}; border: 1px solid #d1d5db; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
                        <strong>{competitor['name']}</strong><br>
                        💰 Цена: {competitor['price']}<br>
                        📚 Тип: {competitor['type']}<br>
                        ⏱️ Длительность: {competitor['duration']}
                    </div>
                    """, unsafe_allow_html=True)
                
                # График цен
                prices_df = pd.DataFrame([
                    {"Конкурент": "А", "Цена": 29900},
                    {"Конкурент": "Б", "Цена": 49900}, 
                    {"Конкурент": "В", "Цена": 19900},
                    {"Конкурент": "Г", "Цена": 79900},
                    {"Конкурент": "Ваш", "Цена": 39900}
                ])
                
                fig = px.bar(prices_df, x='Конкурент', y='Цена', 
                           title="Сравнение цен в нише",
                           color='Конкурент',
                           color_discrete_map={'Ваш': '#10b981'})
                st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📈 Тренды недели")
        
        trends = [
            "Видео-отзывы студентов показывают +40% к вовлечению",
            "Слово 'гарантия' в заголовке повышает CTR на 25%",
            "Креативы с конкретными цифрами работают на 15% лучше",
            "Формат 'До и После' набирает популярность",
            "Акцент на быстрые результаты (7-14 дней) увеличивает конверсию"
        ]
        
        for i, trend in enumerate(trends, 1):
            st.markdown(f"""
            <div class="trend-item">
                <strong>#{i}</strong> {trend}
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.header("🎨 Генератор креативов")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader("📝 Информация о продукте")
        
        product_name = st.text_input("Название курса", placeholder="Курс по Instagram-маркетингу")
        target_audience = st.text_input("Целевая аудитория", placeholder="Предприниматели 25-40 лет")
        price = st.text_input("Цена курса", placeholder="39,900₽")
        unique_value = st.text_area("Главная выгода", placeholder="Что получит студент?")
        
        # Генератор заголовков
        st.subheader("✨ Генератор заголовков")
        
        headline_style = st.selectbox(
            "Стиль заголовка",
            ["Эмоциональный", "Рациональный", "Провокационный", "С цифрами", "Срочность"]
        )
        
        if st.button("🚀 Сгенерировать заголовки", type="primary"):
            with st.spinner("Генерируем заголовки..."):
                headlines = {
                    "Эмоциональный": [
                        f"Устали работать на других? Освойте {product_name}!",
                        f"Мечтаете о свободе? {product_name} - ваш путь к успеху",
                        f"Хватит откладывать! Начните зарабатывать с {product_name}"
                    ],
                    "Рациональный": [
                        f"{product_name}: пошаговая система заработка",
                        f"Изучите {product_name} за 3 месяца. Результат гарантирован",
                        f"Практический {product_name} с реальными кейсами"
                    ],
                    "Провокационный": [
                        f"Почему 90% не зарабатывают в интернете? {product_name} даст ответ",
                        f"Секрет, который скрывают гуру {product_name}",
                        f"Что если я скажу, что {product_name} изменит вашу жизнь?"
                    ],
                    "С цифрами": [
                        f"От 0 до 100,000₽ в месяц с {product_name}",
                        f"7 дней до первого результата в {product_name}",
                        f"2,847 студентов уже освоили {product_name}"
                    ],
                    "Срочность": [
                        f"Последние 3 дня! {product_name} со скидкой 50%",
                        f"Только до конца месяца: {product_name} за {price}",
                        f"Осталось 5 мест на {product_name}. Успейте!"
                    ]
                }
                
                st.success("✅ Заголовки готовы!")
                
                selected_headlines = headlines.get(headline_style, headlines["Эмоциональный"])
                
                for i, headline in enumerate(selected_headlines, 1):
                    st.markdown(f"""
                    <div class="headline-variant">
                        <strong>Вариант {i}:</strong><br>
                        "{headline}"
                        <br><br>
                        <small>💯 AI Оценка: {8.5 + i*0.2:.1f}/10</small>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Генератор полного креатива
        st.subheader("📄 Полный креатив")
        
        if st.button("🎨 Создать креатив"):
            with st.spinner("Создаем креатив..."):
                st.success("✅ Креатив готов!")
                
                generated_creative = f"""
                **Заголовок:** Устали работать на других? Освойте {product_name}!
                
                **Основной текст:**
                Представьте: через 3 месяца вы работаете на себя и зарабатываете от 100,000₽ в месяц.
                
                Наш {product_name} - это пошаговая система, которая уже помогла 2,000+ студентам изменить свою жизнь.
                
                ✅ Практические задания каждый день
                ✅ Поддержка кураторов 24/7  
                ✅ Гарантия результата или возврат денег
                ✅ Доступ к закрытому сообществу
                
                **Призыв к действию:** Начать обучение сейчас
                
                **Цена:** {price} (вместо 59,900₽)
                """
                
                st.markdown(generated_creative)
    
    with col2:
        st.subheader("💡 Рекомендации к креативу")
        
        recommendations = [
            "📹 **Формат:** Используйте видео-отзыв студента - конверсия выше на 40%",
            "🎯 **Аудитория:** Добавьте интересы 'онлайн заработок' + 'саморазвитие'",
            "⏰ **Время:** Лучшие показы: вторник-четверг 14:00-18:00",
            "💰 **Бюджет:** Рекомендуемый дневной бюджет: 3,000-5,000₽",
            "🔄 **A/B тест:** Протестируйте 2-3 варианта заголовка",
            "📱 **Платформы:** Facebook (60%) + Instagram (40%) для максимального охвата"
        ]
        
        for rec in recommendations:
            st.markdown(f"• {rec}")
        
        st.divider()
        
        st.subheader("📊 Быстрая оценка")
        st.markdown("""
        **Ваш креатив:**
        - 🎯 Релевантность: 8.5/10
        - 💫 Эмоциональность: 9.2/10  
        - 🔥 Призыв к действию: 8.8/10
        - 📈 Прогноз CTR: 2.8-3.5%
        """)

with tab3:
    st.header("💰 Калькулятор юнит-экономики")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 Параметры вашего курса")
        
        # Основные параметры
        course_price = st.number_input("Цена курса (₽)", value=39900, step=1000)
        conversion_rate = st.slider("Конверсия сайта (%)", 1.0, 10.0, 3.2, 0.1)
        target_cpc = st.number_input("Планируемый CPC (₽)", value=28, step=1)
        
        # Дополнительные параметры
        with st.expander("🔧 Дополнительные параметры"):
            refund_rate = st.slider("Процент возвратов (%)", 0.0, 20.0, 5.0, 0.5)
            additional_sales = st.slider("Допродажи (% от основной цены)", 0, 100, 20, 5)
            cost_per_student = st.number_input("Затраты на студента (₽)", value=2000, step=100)
        
        if st.button("🧮 Рассчитать экономику", type="primary"):
            # Расчеты
            effective_price = course_price * (1 - refund_rate/100) * (1 + additional_sales/100)
            net_revenue = effective_price - cost_per_student
            cpl = target_cpc / (conversion_rate/100)  # Cost Per Lead
            roi = (net_revenue / cpl) * 100
            breakeven_students = 1
            target_students = 100
            required_budget = target_students * cpl
            profit = target_students * (net_revenue - cpl)
            
            st.markdown(f"""
            <div class="calculator-result">
                <h3>📈 Результаты расчета</h3>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    <div>
                        <strong>💰 Финансы:</strong><br>
                        • Эффективная цена: {effective_price:,.0f}₽<br>
                        • Чистая прибыль с студента: {net_revenue:,.0f}₽<br>
                        • Цена лида: {cpl:,.0f}₽<br>
                        • ROI: {roi:.0f}%
                    </div>
                    <div>
                        <strong>📊 Планирование:</strong><br>
                        • Бюджет на 100 студентов: {required_budget:,.0f}₽<br>
                        • Прибыль с 100 студентов: {profit:,.0f}₽<br>
                        • Окупаемость: {'Мгновенная' if roi > 100 else f'{100/roi*100:.0f}%'}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Графики
            st.subheader("📈 Визуализация воронки")
            
            # Воронка продаж
            funnel_data = pd.DataFrame({
                'Этап': ['Клики', 'Лиды', 'Продажи', 'Активные студенты'],
                'Количество': [
                    int(target_students / (conversion_rate/100)),
                    target_students,
                    int(target_students * (1 - refund_rate/100)),
                    int(target_students * (1 - refund_rate/100) * 0.9)
                ],
                'Стоимость': [required_budget, required_budget, 0, 0]
            })
            
            fig = px.funnel(funnel_data, x='Количество', y='Этап', 
                           title="Воронка продаж (для 100 студентов)")
            st.plotly_chart(fig, use_container_width=True)
            
            # График окупаемости
            students_range = list(range(1, 101))
            revenue_data = [s * net_revenue for s in students_range]
            cost_data = [s * cpl for s in students_range]
            profit_data = [r - c for r, c in zip(revenue_data, cost_data)]
            
            fig_roi = go.Figure()
            fig_roi.add_trace(go.Scatter(x=students_range, y=revenue_data, name='Выручка', line=dict(color='green')))
            fig_roi.add_trace(go.Scatter(x=students_range, y=cost_data, name='Затраты на рекламу', line=dict(color='red')))
            fig_roi.add_trace(go.Scatter(x=students_range, y=profit_data, name='Прибыль', line=dict(color='blue')))
            fig_roi.update_layout(title="Динамика прибыли от количества студентов", 
                                xaxis_title="Количество студентов", yaxis_title="Сумма (₽)")
            st.plotly_chart(fig_roi, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Бенчмарки рынка")
        
        st.markdown("""
        **💡 Средние показатели в нише:**
        
        **Конверсии:**
        - Лендинг: 2-5%
        - Вебинар: 8-15%
        - Личные продажи: 20-40%
        
        **Цены за клик:**
        - Facebook: 20-50₽
        - Google: 30-80₽
        - VK: 15-35₽
        
        **Возвраты:**
        - Стандарт: 5-10%
        - Премиум: 3-7%
        - Бюджетные: 10-20%
        """)
        
        st.subheader("🚀 Рекомендации")
        
        if 'roi' in locals():
            if roi > 200:
                st.success("🔥 Отличная экономика! Можно масштабировать")
            elif roi > 150:
                st.info("✅ Хорошие показатели, есть место для роста")
            elif roi > 100:
                st.warning("⚠️ Минимальная прибыльность, нужна оптимизация")
            else:
                st.error("❌ Убыточная модель, требуется пересмотр")
        
        st.markdown("""
        **💰 Как улучшить экономику:**
        - Повысить конверсию лендинга
        - Снизить CPC через лучший креатив
        - Добавить допродажи
        - Уменьшить процент возвратов
        """)

# Футер
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("🤖 **AI Marketing Co-Pilot v2.0**")
with col2:
    st.markdown(f"🕒 **Обновлено:** {datetime.now().strftime('%d.%m.%Y %H:%M')}")
with col3:
    st.markdown("📧 **Поддержка:** support@ai-marketing.ru")
