whatsapp_agent = """
          This project involved developing an intelligent WhatsApp-based AI assistant designed to streamline the grievance submission and redressal process for citizens. The assistant facilitated user-friendly, multilingual interactions, allowing citizens to submit well-structured, information-rich grievances effortlessly.

          **Key Features and Functionalities:**  
          - **Conversational Interaction:**  
            Citizens could converse with the bot in their preferred language (both text and audio), giving the experience of interacting with a human agent. The bot guided users through the grievance submission process, ensuring all required details were captured effectively.

          - **Spam Detection and Validation:**  
            The assistant incorporated robust spam filtering and user detail verification to ensure only valid grievances were processed. It also validated district and village names using **fuzzy logic** and **LLM function-calling capabilities** to assist users unfamiliar with the exact names of their locations.

          - **Advanced Classification with Custom BERT Model:**  
            Grievances were categorized into one of 100 departments using a **fine-tuned BERT-based classifier** with over **91% accuracy**. The system provided a list of the top 5 probable departments and their confidence scores, enabling informed decision-making.

          - **Enhanced Context Resolution with Azure OpenAI:**  
            For ambiguous cases or low-confidence classifications, the bot leveraged **Azure OpenAI** to prompt users for additional details, ensuring high-quality grievance submissions and reducing misrouting.

          - **Grievance Redressal Optimization:**  
            By providing detailed and accurate grievance information to the correct department, the system reduced average grievance resolution time by **30%**.

          - **Integration with Bhashini for Multilingual Support:**  
            The bot supported multiple languages for both text and audio chats, ensuring inclusivity and accessibility.

         **Impact:**  
          The assistant enabled citizens to raise grievances conveniently while significantly improving the efficiency of the grievance redressal system. By leveraging advanced AI models and intelligent design, it reduced resolution times by **30–40%**, enhanced grievance quality, and ensured accurate routing to appropriate departments, benefiting both users and government grievance redressal officers (GROs).

          This project demonstrates expertise in **AI-driven automation**, **natural language processing**, **multilingual support**, and integration with modern technologies like **Azure OpenAI** and **BERT**, showcasing its scalability and real-world impact.
          """

jalvigil_desc = """ **Optimizing Water Distribution with AI-Powered Analytics**

- **Interactive Dashboard**: Designed using Streamlit and Python to analyze and visualize canal tail performance metrics, leveraging batch-processed data to support efficient water distribution management.  
- **AI-Powered Image Processing**: Fine-tuned **YOLO v7** and implemented **GAN-based models** for accurate tail gauge reading extraction, using **OpenCV** for image orientation correction. This improved overall model accuracy to over **80%** and significantly reduced manual effort.  
- **Impact**: Streamlined water distribution processes and enhanced decision-making for resource allocation.
"""

asha_desc = """**ASHA – Multilingual Voice Assistant for NHAA (Proof of Concept)**

**Empowering SC/ST Communities to Report Atrocities with Ease**

- **Multilingual Voice Assistant**: Built to support the national helpline, enabling SC/ST communities to report atrocities seamlessly.  
- **Advanced AI Integration**: Utilized **Whisper**, **Bhashini**,  for **ASR**, **translation**, **TTS**, and **RAG** for delivering context-specific responses.  
- **User-Centric Logging System**: Designed to track user satisfaction and escalate unresolved queries for prompt action.
 """

autoform_desc = """**Simplifying Form-Filling Processes with Voice-Enabled Assistance**

- **Empowering Citizens**: Accelerated complex form-filling processes and assisted users struggling with language barriers through voice-enabled features.  
- **Advanced NLP Integration**: Leveraged **Whisper**, **Bhashini**, **Azure OpenAI**, and other cutting-edge NLP technologies for seamless user input processing.  
- **Deployment**: Deployed the solution as a **DRF API** using **Docker** on **Azure**, ensuring scalability and robust performance.**
"""

genbi_description = """
**GenBI – AI-Powered Data Exploration via Text-to-SQL and Automated Visualization**  

**Overview:**  
GenBI is an advanced AI agent that enables seamless data exploration by transforming **natural language queries into SQL queries**, performing **data transformations**, and generating **insightful visualizations**—without requiring SQL, Python, or data visualization expertise.    

**Challenges & Innovations:**  

1. **Efficient Database Understanding:**  
   Traditional SQL agents rely on a trial-and-error mechanism to explore tables, leading to **high token consumption and hallucinations**.  
   - **Solution:** Implemented a **database taxonomy system**, storing **metadata, column descriptions, and table embeddings in a Vectorstore**. This allows the agent to **efficiently identify the most relevant tables** through semantic search on the basis of refined user queries and without redundant exploration.  

2. **Optimized SQL Query Generation:**  
   Generating **accurate, efficient SQL queries** tailored to diverse database structures was challenging.  
   - **Solution:** Used **intensive few-shot prompting** and **custom constraints prompts** to ensure high-quality query generation.  

3. **Automated Data Transformation & Visualization:**  
   Typically, users need additional **Python expertise** to process and visualize query results.  
   - **Solution:** Leveraged **LLM function calling** to dynamically generate and execute Python code using **Pandas, NumPy, Matplotlib, and Plotly**, ensuring **high-quality data transformations and meaningful visualizations**.  

4. **Conversational Continuity & Follow-ups:**  
   Handling **multi-turn queries** while maintaining data context is challenging.  
   - **Solution:** Designed a **context-aware short chat history mechanism**, enabling follow-up queries while ensuring responses remain **fact-based and grounded in retrieved data**.  

**Impact:**  
- **Reduced the need for SQL and Python expertise**, making data-driven insights **accessible to non-technical users**.  
- **Reduced token consumption and eliminated LLM hallucinations** by leveraging structured metadata.  
- Enabled **automated, accurate, and context-aware SQL querying, data transformation, visualization and report generation**.  
- Ensured **reliable and conversational AI interactions**, with strong fact-based responses and robust follow-up handling.  
"""


chakshu_desc= """
**Chakshu** is an advanced **OCR-based tool** designed to extract text from **scanned documents**, handling **diverse layouts**, **complex tables spanning multiple pages**, and **structured text formatting**. The system leverages **YOLO** for precise **paragraph and table detection**, coupled with **Tesseract OCR** for text extraction. To ensure accurate parsing, **LLaMA 3.1 (8-bit quantized)** refines the extracted content into structured formats like **Markdown and HTML**. A key innovation in this project is the **fine-tuning of YOLO** on the *USA-Jurisdiction-Adobe-Annotations (2022-07-07)* dataset, enhancing **paragraph-wise text detection**. Additionally, extensive **prompt engineering** ensures **high-quality, context-aware text extraction**. **Chakshu** is a **innovative solution** for **seamless document digitization**, offering **improved accuracy and structured output** across varied document types.
"""