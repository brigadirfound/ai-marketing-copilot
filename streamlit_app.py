import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import asyncio
import requests

# Page config
st.set_page_config(
    page_title="AI Marketing Co-Pilot",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 2rem;
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
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎯 AI Marketing Co-Pilot</h1>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("🔧 Settings")
    
    # API Configuration
    with st.expander("🔑 API Keys"):
        fb_token = st.text_input("Facebook Access Token", type="password")
        google_token = st.text_input("Google Ads Token", type="password")
        getcourse_token = st.text_input("GetCourse API Key", type="password")
    
    # Campaign Selection
    st.header("📊 Campaign Filter")
    date_range = st.date_input(
        "Date Range",
        value=[datetime.now() - timedelta(days=30), datetime.now()],
        max_value=datetime.now()
    )
    
    niche_filter = st.selectbox(
        "Niche",
        ["All", "Digital Marketing", "Programming", "Design", "Business", "Languages"]
    )

# Main Content
col1, col2, col3, col4 = st.columns(4)

# Sample data for demo
sample_metrics = {
    "CPL": {"value": "$12.50", "change": -15, "color": "green"},
    "ROAS": {"value": "320%", "change": 8, "color": "green"}, 
    "CTR": {"value": "2.4%", "change": -5, "color": "red"},
    "Conversion": {"value": "3.2%", "change": 12, "color": "green"}
}

# Metrics Cards
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

# Main Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🕵️ Competitor Analysis", "🎨 Creative Generator", "📈 Campaign Optimizer", "🤖 AI Insights"])

with tab1:
    st.header("🕵️ Competitor Intelligence")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        competitor_url = st.text_input(
            "Enter competitor URL or Facebook page",
            placeholder="https://example.com or @competitorpage"
        )
        
        if st.button("🔍 Analyze Competitor", type="primary"):
            with st.spinner("Analyzing competitor..."):
                # Mock analysis - в реальности здесь MCP call
                st.success("Analysis complete!")
                
                # Sample competitor data
                competitor_data = {
                    "Ad Spend (estimated)": "$15,000/month",
                    "Active Campaigns": "12",
                    "Top Performing Creative": "Video testimonial",
                    "Main Audiences": "25-35, Interests: Online Learning",
                    "Average CPC": "$0.85",
                    "Landing Page Score": "8.2/10"
                }
                
                for key, value in competitor_data.items():
                    st.markdown(f"**{key}:** {value}")
    
    with col2:
        st.subheader("🏆 Top Creatives")
        
        # Mock creative data
        creatives = [
            {"type": "Video", "engagement": "4.2K", "format": "Testimonial"},
            {"type": "Carousel", "engagement": "3.8K", "format": "Before/After"},
            {"type": "Single Image", "engagement": "2.1K", "format": "Infographic"}
        ]
        
        for creative in creatives:
            st.markdown(f"""
            <div class="competitor-card">
                <strong>{creative['type']}</strong><br>
                Engagement: {creative['engagement']}<br>
                Format: {creative['format']}
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.header("🎨 AI Creative Generator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Generate Ad Copy")
        
        product_name = st.text_input("Your Course/Product Name")
        target_audience = st.text_input("Target Audience")
        unique_value = st.text_area("Unique Value Proposition")
        
        if st.button("✨ Generate Creative", type="primary"):
            with st.spinner("Generating creative variations..."):
                # Mock generated creatives
                st.success("Generated 5 creative variations!")
                
                generated_ads = [
                    {
                        "headline": f"Master {product_name} in 30 Days",
                        "description": "Join 10,000+ students who transformed their skills",
                        "cta": "Start Learning Today"
                    },
                    {
                        "headline": f"From Beginner to Pro: {product_name}",
                        "description": "Step-by-step system with real results",
                        "cta": "Get Instant Access"
                    }
                ]
                
                for i, ad in enumerate(generated_ads, 1):
                    with st.expander(f"Creative Variation #{i}"):
                        st.write(f"**Headline:** {ad['headline']}")
                        st.write(f"**Description:** {ad['description']}")
                        st.write(f"**CTA:** {ad['cta']}")
    
    with col2:
        st.subheader("📊 Creative Performance Predictor")
        
        # Mock prediction data
        prediction_data = pd.DataFrame({
            'Creative Type': ['Video Testimonial', 'Carousel', 'Single Image', 'UGC Video'],
            'Predicted CTR': [3.2, 2.8, 2.1, 4.1],
            'Predicted CPC': [0.65, 0.72, 0.89, 0.58]
        })
        
        fig = px.scatter(
            prediction_data, 
            x='Predicted CPC', 
            y='Predicted CTR',
            size='Predicted CTR',
            color='Creative Type',
            title="Creative Performance Prediction"
        )
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("📈 Campaign Optimizer")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Audience Recommendations")
        
        audiences = [
            {"name": "Lookalike 1% - High Value Customers", "score": 9.2, "size": "2.1M"},
            {"name": "Interest: Online Courses + Behavior: Online Spenders", "score": 8.7, "size": "890K"},
            {"name": "Custom: Website Visitors (30 days)", "score": 8.9, "size": "45K"}
        ]
        
        for audience in audiences:
            st.markdown(f"""
            **{audience['name']}**
            - AI Score: {audience['score']}/10
            - Audience Size: {audience['size']}
            """)
    
    with col2:
        st.subheader("💰 Budget Allocation")
        
        # Sample budget data
        budget_data = pd.DataFrame({
            'Campaign': ['Facebook Ads', 'Google Ads', 'VK Ads', 'Yandex'],
            'Current': [40, 35, 15, 10],
            'Recommended': [45, 30, 15, 10]
        })
        
        fig = go.Figure(data=[
            go.Bar(name='Current', x=budget_data['Campaign'], y=budget_data['Current']),
            go.Bar(name='AI Recommended', x=budget_data['Campaign'], y=budget_data['Recommended'])
        ])
        fig.update_layout(barmode='group', title="Budget Allocation (%)")
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.header("🤖 AI Insights & Recommendations")
    
    # AI Insights
    insights = [
        {
            "type": "🚀 Opportunity",
            "title": "Underpriced Keyword Found",
            "description": "The keyword 'online course creation' has 40% lower CPC than similar terms. Recommend increasing budget by $500/month.",
            "impact": "Potential 25% increase in qualified leads"
        },
        {
            "type": "⚠️ Alert", 
            "title": "Creative Fatigue Detected",
            "description": "Your main video creative shows 15% CTR decline over last 7 days. Time to refresh creative.",
            "impact": "Immediate action needed to prevent CPC increase"
        },
        {
            "type": "📊 Insight",
            "title": "Best Performing Time Slot",
            "description": "Tuesday 2-4 PM shows 35% higher conversion rate. Consider increasing bids for this time window.",
            "impact": "Could improve ROAS by 12-18%"
        }
    ]
    
    for insight in insights:
        st.markdown(f"""
        <div class="insight-box">
            <h4>{insight['type']} {insight['title']}</h4>
            <p>{insight['description']}</p>
            <small><strong>Expected Impact:</strong> {insight['impact']}</small>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # AI Chat Interface
    st.subheader("💬 Ask AI Marketing Expert")
    
    user_question = st.text_input("Ask anything about your marketing performance...")
    
    if user_question:
        with st.spinner("AI is analyzing..."):
            # Mock AI response
            ai_response = f"""
            Based on your current campaign data and market trends, here's my analysis:
            
            For the question: "{user_question}"
            
            📊 **Data Insight:** Your campaigns are performing above industry average (CTR: 2.4% vs 1.8% average)
            
            🎯 **Recommendation:** Consider testing video testimonials - competitors in your niche see 40% higher engagement with this format
            
            📈 **Next Steps:**
            1. A/B test new creative format
            2. Increase budget for top-performing audiences
            3. Monitor results over next 7 days
            """
            
            st.markdown(ai_response)

# Footer
st.divider()
st.markdown("🤖 **Powered by Claude 4 + MCP** | Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
