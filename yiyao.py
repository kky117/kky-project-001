import streamlit as st
from openai import OpenAI

# ====================== 你的配置 ======================
API_KEY = "sk-6e63568d256f4d0e932b7cbadc91cf86"
# ======================================================

client = OpenAI(
    api_key=API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 页面标题
st.title("🏥 AI 医药健康小助手")
st.markdown("---")

# ====================== 第一部分：症状诊断 ======================
st.subheader("1️⃣ 症状诊断")
symptom = st.text_input("请描述你的症状：", placeholder="例如：发烧、咳嗽、喉咙痛")

if st.button("🔍 AI 智能诊断"):
    if symptom:
        with st.spinner("AI 分析中..."):
            prompt = f"""
你是专业家庭医生助手，请根据症状给出简洁专业的建议。
用户症状：{symptom}

请按格式输出：
【初步判断】
【建议用药】
【生活建议】
【重要提醒】本建议仅供参考，不能替代医生诊断
"""
            res = client.chat.completions.create(
                model="qwen3.5-35b-a3b",
                messages=[{"role": "user", "content": prompt}]
            )
            st.success("✅ 诊断完成")
            st.write(res.choices[0].message.content)

st.markdown("---")

# ====================== 第二部分：药品说明查询（你要的新功能） ======================
st.subheader("2️⃣ 药品说明书查询")
drug_name = st.text_input("请输入药名：", placeholder="例如：布洛芬、感冒灵、对乙酰氨基酚")

if st.button("📄 查看药品说明"):
    if drug_name:
        with st.spinner("正在查询药品说明..."):
            prompt = f"""
请详细说明【{drug_name}】的使用说明，严格按以下格式输出：

【药品名称】
【适应症】
【用法用量】
【注意事项】
【温馨提示】具体请遵医嘱或按药品说明书服用
"""
            res = client.chat.completions.create(
                model="qwen-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.success("✅ 药品说明如下")
            st.write(res.choices[0].message.content)

st.markdown("---")
st.caption("⚕️ 本工具仅供健康参考，不替代执业医师诊断")
