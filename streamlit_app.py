import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import asyncio
import requests

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
    }
    .success-box {
        background: #dcfce7;
        border: 1px solid #16a34a;
        padding: 1rem;
        border-radius: 8px;
        color: #166534;
    }
    .warning-box {
        background: #fef3c7;
        border: 1px solid #d97706;
        padding: 1rem;
        border-radius: 8px;
        color: #92400e;
    }
</style>
""", unsafe_allow_html=True)

# Заголовок
st.markdown('<h1 class="main-header">🎯 AI Маркетинг Помощник для Онлайн Школ</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #6b7280; font-size: 1.2rem;">Анализ конкурентов • Генерация креативов • Оптимизация рекламы</p>', unsafe_allow_html=True)

# Боковая панель
with st.sidebar:
    st.header("🔧 Настройки")
    
    # Конфигурация API
    with st.expander("🔑 API Ключи"):
        fb_token = st.text_input("Facebook Access Token", type="password", help="Токен для анализа рекламы в Facebook")
        google_token = st.text_input("Google Ads Token", type="password", help="Токен для анализа Google Рекламы")
        getcourse_token = st.text_input("GetCourse API Key", type="password", help="Ключ для интеграции с GetCourse")
        vk_token = st.text_input("VK Ads Token", type="password", help="Токен для анализа рекламы ВКонтакте")
    
    # Фильтры кампаний
    st.header("📊 Фильтры анализа")
    date_range = st.date_input(
        "Период анализа",
        value=[datetime.now() - timedelta(days=30), datetime.now()],
        max_value=datetime.now(),
        help="Выберите период для анализа данных"
    )
    
    niche_filter = st.selectbox(
        "Ниша",
        ["Все ниши", "Цифровой маркетинг", "Программирование", "Дизайн", "Бизнес", "Языки", "Психология", "Фитнес"]
    )
    
    st.divider()
    
    # Быстрые действия
    st.header("⚡ Быстрые действия")
    if st.button("🔄 Обновить все данные"):
        st.success("Данные обновлены!")
    
    if st.button("📧 Отправить отчет"):
        st.info("Отчет отправлен на email!")

# Основной контент
col1, col2, col3, col4 = st.columns(4)

# Примерные метрики для демо
sample_metrics = {
    "Цена лида": {"value": "1,250₽", "change": -15, "color": "green"},
    "ROAS": {"value": "320%", "change": 8, "color": "green"}, 
    "CTR": {"value": "2.4%", "change": -5, "color": "red"},
    "Конверсия": {"value": "3.2%", "change": 12, "color": "green"}
}

# Карточки метрик
for i, (metric, data) in enumerate(sample_metrics.items()):
    with [col1, col2, col3, col4][i]:
        delta_color = "normal" if data["color"] == "green" else "inverse"
        st.metric(
            label=metric,
            value=data["value"],
            delta=f"{data['change']:+}%",
            delta_color=delta_color
        )

st.divider()

# Основные вкладки
tab1, tab2, tab3, tab4 = st.tabs(["🕵️ Анализ конкурентов", "🎨 Генератор креативов", "📈 Оптимизация кампаний", "🤖 AI Рекомендации"])

with tab1:
    st.header("🕵️ Разведка конкурентов")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🔍 Анализ конкурента")
        competitor_url = st.text_input(
            "Введите URL конкурента или страницу в соцсетях",
            placeholder="https://example.com или @конкурент",
            help="Можно ввести сайт, страницу ВК, Facebook или Instagram"
        )
        
        analysis_type = st.selectbox(
            "Тип анализа",
            ["Полный анализ", "Только реклама", "Только контент", "Цены и предложения"]
        )
        
        if st.button("🔍 Анализировать конкурента", type="primary"):
            with st.spinner("Анализируем конкурента... Это займет 1-2 минуты"):
                # Мок-анализ - в реальности здесь MCP вызов
                progress_bar = st.progress(0)
                for i in range(100):
                    progress_bar.progress(i + 1)
                    
                st.success("✅ Анализ завершен!")
                
                # Примерные данные конкурента
                competitor_data = {
                    "💰 Рекламный бюджет (оценка)": "450,000₽/месяц",
                    "📱 Активных кампаний": "18 кампаний",
                    "🏆 Лучший креатив": "Видео-отзыв студента",
                    "👥 Основная аудитория": "25-35 лет, интересы: онлайн обучение",
                    "💲 Средняя цена клика": "28₽",
                    "📊 Оценка лендинга": "8.7/10",
                    "🎯 Главное предложение": "Освой профессию за 3 месяца",
                    "📈 Динамика рекламы": "Рост активности +40% за месяц"
                }
                
                for key, value in competitor_data.items():
                    st.markdown(f"**{key}:** {value}")
                
                # Графики анализа
                st.subheader("📈 Динамика активности конкурента")
                
                # Примерные данные для графика
                dates = pd.date_range(start=datetime.now()-timedelta(days=30), end=datetime.now(), freq='D')
                activity_data = pd.DataFrame({
                    'Дата': dates,
                    'Активность рекламы': [20 + i*0.5 + (i%7)*3 for i in range(len(dates))],
                    'Новые креативы': [(i%5)+1 for i in range(len(dates))]
                })
                
                fig = px.line(activity_data, x='Дата', y=['Активность рекламы', 'Новые креативы'], 
                             title="Активность конкурента за последний месяц")
                st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🏆 Топ креативы ниши")
        
        # Мок-данные креативов
        creatives = [
            {"type": "📹 Видео", "engagement": "4,200", "format": "Отзыв студента", "platform": "Facebook"},
            {"type": "🖼️ Карусель", "engagement": "3,800", "format": "До/После", "platform": "Instagram"},
            {"type": "🖼️ Одно изображение", "engagement": "2,100", "format": "Инфографика", "platform": "VK"},
            {"type": "📹 Stories", "engagement": "1,900", "format": "Быстрые результаты", "platform": "Instagram"},
            {"type": "📰 Текстовое", "engagement": "1,500", "format": "Кейс-история", "platform": "Facebook"}
        ]
        
        for i, creative in enumerate(creatives, 1):
            st.markdown(f"""
            <div class="competitor-card">
                <strong>#{i} {creative['type']}</strong><br>
                💫 Вовлечение: {creative['engagement']}<br>
                🎨 Формат: {creative['format']}<br>
                📱 Платформа: {creative['platform']}
            </div>
            """, unsafe_allow_html=True)
        
        st.subheader("💡 Инсайты")
        st.markdown("""
        **🔥 Тренды недели:**
        - Видео-отзывы работают на 40% лучше
        - Слово "гарантия" повышает CTR на 25%
        - Креативы с цифрами в заголовке +15% к конверсии
        """)

with tab2:
    st.header("🎨 Генератор креативов")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Создание рекламного текста")
        
        product_name = st.text_input("Название вашего курса/продукта", placeholder="Например: Курс по Instagram-маркетингу")
        target_audience = st.text_input("Целевая аудитория", placeholder="Например: Предприниматели 25-40 лет")
        unique_value = st.text_area("Уникальное предложение", placeholder="Что особенного в вашем курсе?")
        
        creative_type = st.selectbox(
            "Тип креатива",
            ["Продающий пост", "Видео-скрипт", "Сторис", "Email письмо", "Описание курса"]
        )
        
        platform = st.selectbox(
            "Платформа",
            ["Facebook/Instagram", "ВКонтакте", "Яндекс.Директ", "Google Ads", "Telegram"]
        )
        
        if st.button("✨ Сгенерировать креативы", type="primary"):
            with st.spinner("Генерируем креативы на основе лучших практик..."):
                st.success("🎉 Создано 5 вариантов креативов!")
                
                # Мок-сгенерированные креативы
                generated_ads = [
                    {
                        "title": "🔥 Вариант 1: Эмоциональный",
                        "headline": f"Устали работать на кого-то? Освойте {product_name}",
                        "description": "За 30 дней превратите хобби в источник дохода. 2,000+ довольных студентов уже изменили свою жизнь",
                        "cta": "Начать обучение сейчас",
                        "score": "9.2/10"
                    },
                    {
                        "title": "💰 Вариант 2: Выгода",
                        "headline": f"{product_name}: От 0 до 100,000₽ в месяц",
                        "description": "Пошаговая система заработка. Первые результаты через 14 дней или вернем деньги",
                        "cta": "Получить доступ",
                        "score": "8.8/10"
                    },
                    {
                        "title": "⏰ Вариант 3: Срочность",
                        "headline": "Последние 3 дня! Скидка 50% на курс",
                        "description": f"Только до 31 декабря - {product_name} за полцены. Места ограничены!",
                        "cta": "Забронировать место",
                        "score": "8.5/10"
                    }
                ]
                
                for ad in generated_ads:
                    with st.expander(ad["title"]):
                        st.markdown(f"**Заголовок:** {ad['headline']}")
                        st.markdown(f"**Описание:** {ad['description']}")
                        st.markdown(f"**Призыв к действию:** {ad['cta']}")
                        st.markdown(f"**AI Оценка:** {ad['score']}")
                        
                        col_copy, col_test = st.columns(2)
                        with col_copy:
                            if st.button(f"📋 Копировать", key=f"copy_{ad['title']}"):
                                st.success("Скопировано!")
                        with col_test:
                            if st.button(f"🧪 A/B тест", key=f"test_{ad['title']}"):
                                st.info("Добавлено в план тестирования")
    
    with col2:
        st.subheader("📊 Прогноз эффективности")
        
        # Мок-данные прогноза
        prediction_data = pd.DataFrame({
            'Тип креатива': ['Видео-отзыв', 'Карусель', 'Одно фото', 'UGC видео', 'Анимация'],
            'Прогноз CTR': [3.2, 2.8, 2.1, 4.1, 2.5],
            'Прогноз CPC': [25, 32, 45, 22, 38],
            'Размер аудитории': [2.1, 1.8, 3.2, 1.9, 2.4]
        })
        
        fig = px.scatter(
            prediction_data, 
            x='Прогноз CPC', 
            y='Прогноз CTR',
            size='Размер аудитории',
            color='Тип креатива',
            title="Прогноз эффективности по типам креативов",
            labels={'Прогноз CPC': 'Цена клика (₽)', 'Прогноз CTR': 'CTR (%)'}
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("🎯 Рекомендации по улучшению")
        
        recommendations = [
            "📹 Добавьте видео-отзывы - они повышают доверие на 60%",
            "🔥 Используйте эмодзи в заголовках - рост CTR на 25%",
            "💰 Покажите конкретную выгоду в цифрах",
            "⏰ Добавьте элемент срочности ('Только 3 дня!')",
            "👥 Включите социальные доказательства ('2000+ студентов')"
        ]
        
        for rec in recommendations:
            st.markdown(f"• {rec}")

with tab3:
    st.header("📈 Оптимизация кампаний")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Рекомендации по аудиториям")
        
        audiences = [
            {
                "name": "Lookalike 1% - Покупатели курсов", 
                "score": 9.2, 
                "size": "2.1M", 
                "cpc": "22₽",
                "description": "Похожие на ваших лучших клиентов"
            },
            {
                "name": "Интересы: Онлайн курсы + Поведение: Покупки онлайн", 
                "score": 8.7, 
                "size": "890K", 
                "cpc": "28₽",
                "description": "Активные покупатели обучения"
            },
            {
                "name": "Ретаргетинг: Посетители сайта (30 дней)", 
                "score": 8.9, 
                "size": "45K", 
                "cpc": "18₽",
                "description": "Теплая аудитория с сайта"
            }
        ]
        
        for audience in audiences:
            st.markdown(f"""
            <div class="competitor-card">
                <strong>{audience['name']}</strong><br>
                🏆 AI Оценка: {audience['score']}/10<br>
                👥 Размер: {audience['size']}<br>
                💰 CPC: {audience['cpc']}<br>
                📝 {audience['description']}
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("💰 Распределение бюджета")
        
        # Данные по бюджету
        budget_data = pd.DataFrame({
            'Платформа': ['Facebook/Instagram', 'Google Ads', 'ВКонтакте', 'Яндекс.Директ'],
            'Текущее': [40, 35, 15, 10],
            'Рекомендуется': [45, 30, 15, 10],
            'ROI': [320, 280, 250, 200]
        })
        
        fig = go.Figure(data=[
            go.Bar(name='Текущее распределение', x=budget_data['Платформа'], y=budget_data['Текущее']),
            go.Bar(name='AI Рекомендация', x=budget_data['Платформа'], y=budget_data['Рекомендуется'])
        ])
        fig.update_layout(barmode='group', title="Оптимальное распределение бюджета (%)")
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("⏰ Лучшее время для рекламы")
        
        # График по времени
        time_data = pd.DataFrame({
            'Час': list(range(24)),
            'Конверсия': [1.2, 0.8, 0.5, 0.3, 0.4, 0.8, 1.5, 2.1, 2.8, 3.2, 3.5, 3.8, 
                         3.2, 2.9, 3.1, 3.6, 4.2, 4.8, 4.1, 3.5, 2.8, 2.1, 1.8, 1.5]
        })
        
        fig_time = px.line(time_data, x='Час', y='Конверсия', 
                          title="Конверсия по часам (средняя за неделю)")
        fig_time.add_hline(y=time_data['Конверсия'].mean(), line_dash="dash", 
                          annotation_text="Средняя конверсия")
        st.plotly_chart(fig_time, use_container_width=True)

with tab4:
    st.header("🤖 AI Рекомендации и инсайты")
    
    # AI Инсайты
    insights = [
        {
            "type": "🚀 Возможность",
            "title": "Недооцененное ключевое слово найдено",
            "description": "Ключевое слово 'создание онлайн курсов' имеет цену на 40% ниже похожих. Рекомендуем увеличить бюджет на 15,000₽/месяц.",
            "impact": "Потенциальный рост лидов на 25%",
            "priority": "high"
        },
        {
            "type": "⚠️ Внимание", 
            "title": "Усталость креатива обнаружена",
            "description": "Ваш основной видео-креатив показывает снижение CTR на 15% за последние 7 дней. Время обновить креатив.",
            "impact": "Требуется немедленное действие для предотвращения роста CPC",
            "priority": "urgent"
        },
        {
            "type": "📊 Инсайт",
            "title": "Лучшее время для показов",
            "description": "Вторник 14:00-16:00 показывает конверсию на 35% выше. Рекомендуем увеличить ставки в это время.",
            "impact": "Может улучшить ROAS на 12-18%",
            "priority": "medium"
        },
        {
            "type": "💡 Совет",
            "title": "Новый тренд в нише",
            "description": "Конкуренты начали активно использовать формат 'история успеха за 30 дней'. Конверсия таких креативов выше на 28%.",
            "impact": "Рекомендуем протестировать этот формат",
            "priority": "low"
        }
    ]
    
    for insight in insights:
        priority_color = {"urgent": "#dc2626", "high": "#ea580c", "medium": "#ca8a04", "low": "#16a34a"}
        border_color = priority_color.get(insight["priority"], "#16a34a")
        
        st.markdown(f"""
        <div style="border-left: 4px solid {border_color}; background: #f8fafc; padding: 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0;">
            <h4>{insight['type']} {insight['title']}</h4>
            <p>{insight['description']}</p>
            <small><strong>Ожидаемый эффект:</strong> {insight['impact']}</small>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # AI Чат-интерфейс
    st.subheader("💬 Спросите AI-эксперта по маркетингу")
    
    # Быстрые вопросы
    quick_questions = [
        "Как снизить стоимость лида?",
        "Какие креативы сейчас работают лучше всего?", 
        "Стоит ли увеличивать бюджет на Facebook?",
        "Как улучшить конверсию лендинга?"
    ]
    
    cols = st.columns(2)
    for i, question in enumerate(quick_questions):
        with cols[i % 2]:
            if st.button(f"💡 {question}", key=f"quick_{i}"):
                st.session_state['ai_question'] = question
    
    user_question = st.text_input("Или задайте свой вопрос о маркетинговых показателях...")
    
    # Если есть вопрос (из быстрых или введенный)
    current_question = st.session_state.get('ai_question', user_question)
    
    if current_question:
        with st.spinner("AI анализирует данные..."):
            # Мок AI ответа
            ai_response = f"""
            **Анализ по вопросу:** "{current_question}"
            
            📊 **Анализ данных:** Ваши кампании работают выше среднего по рынку (CTR: 2.4% против 1.8% среднего)
            
            🎯 **Рекомендация:** Протестируйте видео-отзывы клиентов - конкуренты в вашей нише видят рост вовлечения на 40% с таким форматом
            
            📈 **План действий:**
            1. 🧪 A/B тестирование нового формата креативов
            2. 💰 Увеличение бюджета на самые эффективные аудитории  
            3. 📊 Мониторинг результатов в течение 7 дней
            4. 🔄 Корректировка стратегии на основе данных
            
            **💡 Дополнительные советы:**
            - Добавьте больше социальных доказательств в креативы
            - Протестируйте призывы к действию с ограничением по времени
            - Рассмотрите возможность ретаргетинга на посетителей сайта
            """
            
            st.markdown(ai_response)
            
            # Сброс вопроса
            if 'ai_question' in st.session_state:
                del st.session_state['ai_question']
    
    # Раздел с полезными метриками
    st.divider()
    st.subheader("📊 Сравнение с рынком")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🎯 Ваши показатели:**
        - CTR: 2.4% 
        - CPC: 28₽
        - Конверсия: 3.2%
        - ROAS: 320%
        """)
    
    with col2:
        st.markdown("""
        **📈 Средние по рынку:**
        - CTR: 1.8%
        - CPC: 35₽  
        - Конверсия: 2.1%
        - ROAS: 280%
        """)
    
    with col3:
        st.markdown("""
        **🏆 Топ-10% школ:**
        - CTR: 3.8%
        - CPC: 22₽
        - Конверсия: 5.1% 
        - ROAS: 450%
        """)

# Футер
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("🤖 **На базе Claude 4 + MCP технологий**")
with col2:
    st.markdown(f"🕒 **Обновлено:** {datetime.now().strftime('%d.%m.%Y %H:%M')}")
with col3:
    st.markdown("📧 **Поддержка:** support@ai-marketing.ru")

# Скрытая информация для разработки
with st.expander("🔧 Техническая информация"):
    st.markdown("""
    **Статус интеграций:**
    - ✅ Facebook Marketing API - подключено
    - ✅ Google Ads API - подключено  
    - ⏳ VK Ads API - в разработке
    - ⏳ Яндекс.Директ API - в разработке
    - ⏳ GetCourse API - в разработке
    
    **Версия:** MVP 1.0  
    **Последний деплой:** {datetime.now().strftime('%d.%m.%Y %H:%M')}
    """)
