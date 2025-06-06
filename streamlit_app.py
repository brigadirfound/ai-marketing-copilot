import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# Настройка страницы
st.set_page_config(
    page_title="Spy-Tool для Онлайн Школ",
    page_icon="🕵️",
    layout="wide"
)

# Инициализация состояния
if 'search_completed' not in st.session_state:
    st.session_state.search_completed = False
if 'analysis_completed' not in st.session_state:
    st.session_state.analysis_completed = False
if 'selected_schools' not in st.session_state:
    st.session_state.selected_schools = []

# Кастомный CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 1rem;
        text-align: center;
    }
    .subtitle {
        font-size: 1.4rem;
        color: #6b7280;
        text-align: center;
        margin-bottom: 3rem;
    }
    .search-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 2rem 0;
    }
    .school-card {
        border: 2px solid #e5e7eb;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        background: #f9fafb;
        transition: all 0.3s ease;
    }
    .school-card:hover {
        border-color: #3b82f6;
        background: #eff6ff;
    }
    .school-card.selected {
        border-color: #10b981;
        background: #ecfdf5;
    }
    .insight-box {
        background: #fef3c7;
        border-left: 4px solid #f59e0b;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    .review-card {
        background: white;
        border: 1px solid #e5e7eb;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.8rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .social-post {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.8rem 0;
    }
    .competitor-tab {
        background: white;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .metric-big {
        font-size: 2rem;
        font-weight: 700;
        color: #1f2937;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #6b7280;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# Заголовок
st.markdown('<h1 class="main-header">🕵️ Spy-Tool для Онлайн Школ</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Найди конкурентов → Проанализируй их фишки → Создай лучшие креативы</p>', unsafe_allow_html=True)

# Если анализ не начат - показываем поиск
if not st.session_state.search_completed:
    
    st.markdown("""
    <div class="search-section">
        <h2 style="color: white; margin-bottom: 1rem;">🔍 Найди конкурентов в своей нише</h2>
        <p style="color: #e0e7ff;">Выбери нишу и настрой фильтры - мы найдем всех твоих конкурентов и проанализируем их стратегии</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🎯 Выбери нишу")
        
        niche = st.selectbox(
            "Основная ниша",
            [
                "Digital-маркетинг & SMM",
                "Программирование & IT", 
                "Дизайн & Графика",
                "Бизнес & Предпринимательство",
                "Психология & Личностный рост",
                "Языки & Лингвистика",
                "Фитнес & Здоровье",
                "Финансы & Инвестиции",
                "Кулинария & Хобби",
                "Красота & Стиль"
            ]
        )
        
        keywords = st.text_input(
            "🔑 Дополнительные ключевые слова",
            placeholder="курс маркетинг, SMM обучение, таргетинг"
        )
        
    with col2:
        st.subheader("⚙️ Фильтры")
        
        price_range = st.slider(
            "💰 Ценовой диапазон (₽)",
            5000, 200000, (20000, 80000), 5000
        )
        
        region = st.selectbox(
            "📍 Регион",
            ["Россия", "СНГ", "Весь мир"]
        )
        
        school_size = st.selectbox(
            "📊 Размер школы",
            ["Любой", "Стартап (до 1000 студентов)", "Средняя (1000-10000)", "Крупная (10000+)"]
        )
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔍 Найти конкурентов", type="primary", use_container_width=True):
            with st.spinner("Ищем онлайн школы в нише..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(i + 1)
                
                st.session_state.search_completed = True
                st.rerun()

# Если поиск завершен, но анализ не начат - показываем результаты поиска
elif st.session_state.search_completed and not st.session_state.analysis_completed:
    
    st.markdown("### 🎉 Найдено онлайн школ в вашей нише: **23**")
    
    # Мок-данные школ
    schools_data = [
        {"name": "Skillbox", "niche": "Дизайн", "price": "49,900₽", "students": "50,000+", "rating": "4.2", "url": "skillbox.ru"},
        {"name": "GeekBrains", "niche": "Программирование", "price": "89,900₽", "students": "100,000+", "rating": "4.1", "url": "geekbrains.ru"},
        {"name": "Нетология", "niche": "Маркетинг", "price": "39,900₽", "students": "200,000+", "rating": "4.4", "url": "netology.ru"},
        {"name": "TexTerra", "niche": "Контент-маркетинг", "price": "29,900₽", "students": "5,000+", "rating": "4.7", "url": "texterra.ru"},
        {"name": "Convertmonster", "niche": "Таргетинг", "price": "59,900₽", "students": "15,000+", "rating": "4.5", "url": "convertmonster.ru"},
        {"name": "WebCanape", "niche": "SMM", "price": "24,900₽", "students": "8,000+", "rating": "4.3", "url": "webcanape.ru"},
        {"name": "ProductStar", "niche": "Продуктовый менеджмент", "price": "79,900₽", "students": "25,000+", "rating": "4.6", "url": "productstar.ru"},
        {"name": "Eduson Academy", "niche": "Бизнес", "price": "45,900₽", "students": "12,000+", "rating": "4.0", "url": "eduson.tv"}
    ]
    
    st.markdown("**📋 Выберите школы для анализа** (выберите 3-5 школ для получения максимальных инсайтов):")
    
    # Создаем чекбоксы для выбора школ
    for i, school in enumerate(schools_data):
        checkbox_key = f"school_{i}"
        
        selected = st.checkbox(
            f"**{school['name']}** • {school['niche']} • {school['price']} • {school['students']} студентов • ⭐ {school['rating']}",
            key=checkbox_key
        )
        
        if selected and school not in st.session_state.selected_schools:
            st.session_state.selected_schools.append(school)
        elif not selected and school in st.session_state.selected_schools:
            st.session_state.selected_schools.remove(school)
    
    st.markdown("---")
    
    selected_count = len(st.session_state.selected_schools)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if selected_count > 0:
            if st.button(f"🚀 Анализировать выбранные школы ({selected_count})", type="primary", use_container_width=True):
                with st.spinner(f"Анализируем {selected_count} школ... Это займет 2-3 минуты"):
                    progress_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.03)
                        progress_bar.progress(i + 1)
                    
                    st.session_state.analysis_completed = True
                    st.rerun()
        else:
            st.warning("⚠️ Выберите хотя бы одну школу для анализа")

# Если анализ завершен - показываем результаты
else:
    
    st.markdown("## 🎯 Анализ конкурентов завершен!")
    st.markdown(f"**Проанализировано школ:** {len(st.session_state.selected_schools)}")
    
    # Общая статистика
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<p class="metric-label">Средняя цена</p>', unsafe_allow_html=True)
        st.markdown('<p class="metric-big">52,400₽</p>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<p class="metric-label">Диапазон цен</p>', unsafe_allow_html=True)
        st.markdown('<p class="metric-big">24,900₽ - 89,900₽</p>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<p class="metric-label">Средний рейтинг</p>', unsafe_allow_html=True)
        st.markdown('<p class="metric-big">⭐ 4.3</p>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<p class="metric-label">Общий охват</p>', unsafe_allow_html=True)
        st.markdown('<p class="metric-big">450,000+ студентов</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Выбираем конкурента для детального анализа
    st.subheader("🔍 Детальный анализ конкурента")
    
    selected_competitor = st.selectbox(
        "Выберите школу для детального анализа:",
        [school['name'] for school in st.session_state.selected_schools]
    )
    
    # Поиск выбранной школы
    competitor_data = next((school for school in st.session_state.selected_schools if school['name'] == selected_competitor), None)
    
    if competitor_data:
        
        # Вкладки анализа
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Общая информация", "⭐ Отзывы и репутация", "📱 Соцсети", "🎨 Генератор креативов"])
        
        with tab1:
            st.markdown(f"### 📊 Анализ школы: **{competitor_data['name']}**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                **🏢 Основная информация:**
                - Сайт: {competitor_data['url']}
                - Ниша: {competitor_data['niche']}
                - Цена курсов: {competitor_data['price']}
                - Количество студентов: {competitor_data['students']}
                - Рейтинг: ⭐ {competitor_data['rating']}/5
                
                **📈 Анализ трафика:**
                - Посещений в месяц: ~250,000
                - Источники трафика: Поиск (45%), Реклама (35%), Прямые (20%)
                - Ключевые слова: курсы {competitor_data['niche'].lower()}, обучение онлайн
                """)
            
            with col2:
                st.markdown(f"""
                **🎯 Маркетинговая стратегия:**
                - Основной канал: Facebook + Instagram
                - Рекламный бюджет: ~500,000₽/месяц
                - Главный оффер: "Освой профессию за 4 месяца"
                - USP: Гарантия трудоустройства
                
                **💰 Ценообразование:**
                - Базовый тариф: {competitor_data['price']}
                - Рассрочка: 12 месяцев
                - Скидки: до 50% на Black Friday
                - Средний чек: 65,000₽
                """)
            
            # График активности
            st.subheader("📈 Активность конкурента")
            
            dates = pd.date_range(start=datetime.now()-timedelta(days=30), end=datetime.now(), freq='D')
            activity_data = pd.DataFrame({
                'Дата': dates,
                'Рекламная активность': [20 + i*0.5 + (i%7)*3 for i in range(len(dates))],
                'Новые посты': [(i%5)+1 for i in range(len(dates))]
            })
            
            fig = px.line(activity_data, x='Дата', y=['Рекламная активность', 'Новые посты'], 
                         title=f"Активность {competitor_data['name']} за последний месяц")
            st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.markdown(f"### ⭐ Отзывы и репутация: **{competitor_data['name']}**")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.subheader("📊 Анализ отзывов")
                
                # Источники отзывов
                review_sources = pd.DataFrame({
                    'Источник': ['Otzovik', 'VK группа', 'Яндекс.Карты', 'Google', 'IRecommend'],
                    'Количество отзывов': [45, 128, 67, 89, 23],
                    'Средний рейтинг': [4.2, 4.4, 4.1, 4.3, 4.0]
                })
                
                fig = px.bar(review_sources, x='Источник', y='Количество отзывов', 
                           color='Средний рейтинг', 
                           title="Отзывы по источникам")
                st.plotly_chart(fig, use_container_width=True)
                
                st.subheader("💬 Примеры отзывов")
                
                reviews = [
                    {
                        "author": "Анна К.", 
                        "rating": "⭐⭐⭐⭐⭐",
                        "text": "Отличный курс! За 3 месяца освоила таргетинг с нуля. Преподаватели объясняют понятно, много практики.",
                        "source": "Otzovik",
                        "sentiment": "positive"
                    },
                    {
                        "author": "Дмитрий М.", 
                        "rating": "⭐⭐⭐",
                        "text": "Курс неплохой, но дороговато. Можно было бы больше актуальных кейсов добавить.",
                        "source": "VK",
                        "sentiment": "neutral"
                    },
                    {
                        "author": "Елена С.", 
                        "rating": "⭐⭐",
                        "text": "Разочарована. Обещали помочь с трудоустройством, но поддержки почти нет.",
                        "source": "Google",
                        "sentiment": "negative"
                    }
                ]
                
                for review in reviews:
                    sentiment_color = {"positive": "#dcfce7", "neutral": "#fef3c7", "negative": "#fecaca"}
                    color = sentiment_color.get(review["sentiment"], "#f9fafb")
                    
                    st.markdown(f"""
                    <div style="background: {color}; border: 1px solid #e5e7eb; padding: 1rem; border-radius: 8px; margin: 0.8rem 0;">
                        <strong>{review['author']}</strong> • {review['rating']} • {review['source']}<br>
                        "{review['text']}"
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.subheader("🔍 Инсайты из отзывов")
                
                st.markdown("""
                **😊 ТОП ПОХВАЛ:**
                • Качественная подача материала (67%)
                • Много практических заданий (54%) 
                • Отзывчивые кураторы (48%)
                • Актуальная информация (41%)
                
                **😞 ТОП ЖАЛОБ:**
                • Высокая цена (34%)
                • Слабая поддержка трудоустройства (28%)
                • Мало обратной связи (22%)
                • Устаревшие кейсы (18%)
                
                **💡 ВОЗМОЖНОСТИ ДЛЯ ВАС:**
                ✅ Сделать цену на 20% ниже
                ✅ Акцент на помощь с трудоустройством
                ✅ Персональная обратная связь
                ✅ Свежие кейсы 2024 года
                """)
                
                st.markdown("---")
                
                st.subheader("📈 Sentiment анализ")
                
                sentiment_data = pd.DataFrame({
                    'Тип': ['Позитивные', 'Нейтральные', 'Негативные'],
                    'Процент': [65, 25, 10]
                })
                
                fig_pie = px.pie(sentiment_data, values='Процент', names='Тип',
                               color_discrete_map={'Позитивные': '#10b981', 'Нейтральные': '#f59e0b', 'Негативные': '#ef4444'})
                st.plotly_chart(fig_pie, use_container_width=True)
        
        with tab3:
            st.markdown(f"### 📱 Соцсети: **{competitor_data['name']}**")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("👥 VK группа")
                st.markdown("""
                **📊 Статистика:**
                - Подписчики: 45,600
                - Охват постов: 3,000-8,000
                - Частота: 3-4 поста в день
                - Лучшее время: 10:00, 14:00, 18:00
                """)
                
                st.subheader("🔥 Популярные посты")
                
                vk_posts = [
                    {"content": "Кейс студента: увеличил продажи на 300% за месяц", "likes": 450, "comments": 67},
                    {"content": "Бесплатный вебинар: 5 ошибок в таргетинге", "likes": 320, "comments": 89}, 
                    {"content": "Скидка 40% только до конца недели!", "likes": 280, "comments": 34}
                ]
                
                for post in vk_posts:
                    st.markdown(f"""
                    <div class="social-post">
                        <strong>VK:</strong> "{post['content']}"<br>
                        <small>❤️ {post['likes']} • 💬 {post['comments']}</small>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.subheader("📸 Instagram")
                st.markdown("""
                **📊 Статистика:**
                - Подписчики: 28,900
                - Охват Stories: 5,000-12,000
                - Частота: 1-2 поста + Stories ежедневно
                - ER: 4.2% (хороший показатель)
                """)
                
                st.subheader("📈 Популярный контент")
                
                instagram_posts = [
                    {"content": "До/После: портфолио студента-дизайнера", "likes": 890, "type": "Карусель"},
                    {"content": "Stories: быстрые советы по SMM", "views": 6500, "type": "Stories"},
                    {"content": "Reels: день из жизни SMM-щика", "likes": 1200, "type": "Video"}
                ]
                
                for post in instagram_posts:
                    metric = f"👁️ {post['views']}" if 'views' in post else f"❤️ {post['likes']}"
                    st.markdown(f"""
                    <div class="social-post">
                        <strong>IG:</strong> "{post['content']}"<br>
                        <small>{post['type']} • {metric}</small>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            st.subheader("💡 Инсайты для вашей стратегии")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                **🎯 Что копировать:**
                • Кейсы студентов - самый популярный контент
                • Бесплатные вебинары для привлечения
                • Stories с быстрыми советами
                • Формат "до/после" работает отлично
                """)
            
            with col2:
                st.markdown("""
                **⏰ Оптимальное время постов:**
                • VK: 10:00, 14:00, 18:00
                • Instagram: 12:00, 19:00, 21:00
                • Stories: 9:00-10:00, 17:00-19:00
                • Reels: 18:00-21:00
                """)
        
        with tab4:
            st.markdown("### 🎨 Генератор креативов")
            st.markdown("*На основе анализа конкурентов создаем ваши уникальные креативы*")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.subheader("📝 Параметры вашего курса")
                
                your_course = st.text_input("Название вашего курса", placeholder="Курс по Instagram-маркетингу PRO")
                your_price = st.text_input("Ваша цена", placeholder="34,900₽")
                your_usp = st.text_area("Ваше уникальное предложение", 
                                      placeholder="Что будет отличать вас от конкурентов?")
                
                creative_type = st.selectbox(
                    "Тип креатива",
                    ["Пост для VK", "Instagram пост", "Stories", "Рекламное объявление", "Email письмо"]
                )
                
                if st.button("✨ Создать креативы", type="primary"):
                    with st.spinner("Анализируем конкурентов и создаем ваши креативы..."):
                        time.sleep(2)
                        
                        st.success("🎉 Креативы готовы!")
                        
                        # Генерируем креативы на основе анализа конкурентов
                        generated_creatives = [
                            {
                                "title": "🔥 Креатив #1: Бьем конкурентов по цене",
                                "headline": f"{your_course} - результат как у {competitor_data['name']}, но на 30% дешевле!",
                                "description": f"Пока {competitor_data['name']} берет {competitor_data['price']}, ты получаешь тот же результат за {your_price}. Почему переплачивать?",
                                "insight": f"💡 Основано на жалобах клиентов {competitor_data['name']} на высокую цену"
                            },
                            {
                                "title": "⭐ Креатив #2: Решаем их слабое место",  
                                "headline": f"Гарантируем трудоустройство или возвращаем 100% денег",
                                "description": f"В отличие от других школ, мы не бросаем студентов после курса. Персональная помощь с поиском работы в течение 6 месяцев.",
                                "insight": f"💡 Основано на жалобах клиентов {competitor_data['name']} на слабую поддержку трудоустройства"
                            },
                            {
                                "title": "🎯 Креатив #3: Копируем их сильные стороны",
                                "headline": f"Кейс студента: +300% к продажам за месяц (как у {competitor_data['name']})",
                                "description": f"Тот же результат, что показывают в {competitor_data['name']}, но с персональным ментором и современными кейсами 2024 года.",
                                "insight": "💡 Основано на самом популярном формате контента конкурентов"
                            }
                        ]
                        
                        for creative in generated_creatives:
                            st.markdown(f"""
                            <div style="background: #f0f9ff; border: 2px solid #0ea5e9; padding: 1.5rem; border-radius: 12px; margin: 1rem 0;">
                                <h4>{creative['title']}</h4>
                                <p><strong>Заголовок:</strong> {creative['headline']}</p>
                                <p><strong>Описание:</strong> {creative['description']}</p>
                                <p><em>{creative['insight']}</em></p>
                            </div>
                            """, unsafe_allow_html=True)
            
            with col2:
                st.subheader("🧠 AI рекомендации")
                
                st.markdown(f"""
                **На основе анализа {competitor_data['name']}:**
                
                **✅ Используйте в креативах:**
                • Кейсы с конкретными цифрами
                • Формат "до/после"  
                • Акцент на гарантии результата
                • Сравнение с конкурентами
                
                **🎯 Оптимальная стратегия:**
                • Цена на 20-30% ниже {competitor_data['name']}
                • Акцент на персональную поддержку
                • Современные кейсы 2024 года
                • Гарантия трудоустройства
                
                **📱 Площадки для запуска:**
                • VK: кейсы студентов
                • Instagram: до/после результаты
                • Facebook: длинные посты с историями
                """)
    
    # Кнопка для нового поиска
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Найти новых конкурентов", use_container_width=True):
            # Сбрасываем состояние
            st.session_state.search_completed = False
            st.session_state.analysis_completed = False
            st.session_state.selected_schools = []
            st.rerun()

# Футер
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("🕵️ **Spy-Tool v3.0** - Анализ конкурентов + Генерация креативов")
with col2:
    st.markdown(f"🕒 **Обновлено:** {datetime.now().strftime('%d.%m.%Y %H:%M')}")
with col3:
    st.markdown("📧 **Поддержка:** support@spy-tool.ru")
