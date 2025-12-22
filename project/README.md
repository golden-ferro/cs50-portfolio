
# Project Title: Customer service automation in N8N

#### Video Demo: https://youtu.be/pI7htliB4BU

#### Description:
This project is a sophisticated, "human-in-the-loop" customer service automation system for WhatsApp. Orchestrated by **n8n** (self-hosted on a Hostinger VPS) and integrated with **Chatwoot**, the system leverages OpenAI's models to handle multimodal communication (text, audio, and images). It features intelligent state management to seamlessly switch between AI and human agents, a buffering system for context preservation, and background maintenance workflows for analytics and database optimization.

## Technology Stack
* **Orchestration:** n8n (Self-hosted on VPS).
* **Customer Engagement Platform:** Chatwoot (via WhatsApp).
* **AI:** OpenAI GPT 5
* **Vector:** Qdrant (for RAG/Semantic Search).
* **Relational:** MySQL (for order history and customer data).
* **Key-Value:** Redis (for state management and message buffering).

## Workflow Architecture (The Logic Flow)

The system is divided into modular workflows to ensure separation of concerns and scalability. The data flows in the following specific order:

### 1. Reception & State Management (Red Flow)
This is the entry point triggered by a Webhook from Chatwoot. Its primary function is **Human-in-the-loop** management:
* **Source Identification:** It identifies whether an incoming message is from the customer or a human agent.
* **Conflict Prevention:** If a human agent replies, the workflow updates a state variable in Redis to "pause" the AI. This prevents the AI from responding over the human agent.
* If the AI is active and the message is from a customer, the data is passed to the next stage.

### 2. Multimodal Normalization (Green Flow)
Since WhatsApp users send various media types, this workflow standardizes inputs before the AI processes them:
* **Audio:** The audio is transcribed into text using an OpenAI model.
* **Images:** Photos are analyzed by an OpenAI model to generate a textual description of the content.
* **Text:** Passed through directly.
* **Output:** A standardized JSON object containing the unified text context is sent to the buffer.

### 3. Message Buffering (Purple Flow)
To handle the "fragmented" messaging style of WhatsApp users (sending multiple short messages in a row), this workflow implements a buffer:
* **Accumulation:** Messages are held in a temporary queue.
* **Timeout:** A timer waits for a defined interval.
* **Concatenation:** Once the time expires, all accumulated messages are joined into a single prompt. This saves API tokens and provides the AI with a complete context rather than fragmented sentences.

### 4. The AI Agent & Response (Blue Flow)
This is the "brain" of the operation. The AI Agent receives the formatted, buffered context and determines the best course of action using specific **Tools**:
* **Short-Term Memory:** Retains the last 5 interactions for conversational continuity.
* **RAG (Vector Database):** Queries **Qdrant** to find relevant product information or support documentation via embeddings.
* **SQL Database:** Accesses MySQL to read customer details or update order statuses.
* **Price Comparison Tool:** A dedicated tool designed to filter and compare product prices for the user.
* **Human Handoff:** If the AI detects negative sentiment or cannot answer, it tags the conversation in Chatwoot to alert a human agent.

---

## Maintenance & Analytics Workflows (Background Processes)

In addition to the real-time chat, the system includes two automated background workflows to ensure long-term health and business intelligence:

### 5. Monthly Insights Generator
* **Trigger:** Runs automatically once a month.
* **Action:** Queries the SQL database to retrieve all interactions and orders from the past month.
* **Analysis:** The AI analyzes this bulk data to generate a structured summary of customer behavior, sales patterns, and relevant insights.
* **Reporting:** This summary is appended to a **Google Sheet** (used strictly for reporting/analytics, not for live chat context) to help the business owner track performance.

### 6. Memory Sanitation
* **Goal:** Database optimization and privacy.
* **Action:** A scheduled task executes an SQL query to delete interaction records that haven't been updated in over a month.
* **Benefit:** This prevents the server memory and database from becoming overloaded with obsolete data, ensuring the system remains fast and responsive.

## Installation & Setup

The project logic is built on n8n. You can find the workflow template files in the [`/workflows`](./workflows) directory.

**How to import:**
1. Download the `.json` files from the `workflows` folder.
2. Open your n8n instance.
3. Go to **Workflows** > **Import from File**.
4. Configure your credentials (OpenAI, MySQL, Redis, Google Sheets) in the respective nodes.
