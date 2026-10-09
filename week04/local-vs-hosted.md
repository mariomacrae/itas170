**Local or hosted? Privacy, security and ethics — the honest table**  
A reference for Part 3's last question and for the rest of your life. "Local"  
   
 means weights on a machine you control (this lab desktop, your laptop, a  
   
 server your organisation owns). "Hosted" means a frontier model behind  
   
 someone else's API or chat window. Facts are as of September 2026 and will  
   
 drift; the trade-offs will not.  
| | | |  
|-|-|-|  
|   | **Local** ** (Ollama on your machine)** | **Hosted frontier** ** (a chat window or API)** |   
| **Where your text goes** | Nowhere. It never leaves the machine. | To the provider's servers, through their logs, under their terms. |   
| **Training on your data** | Never — there is nobody to train. | **API and business plans:** the three big providers do not train on your data by default and keep abuse-monitoring logs about 30 days.  **Consumer chat apps:** training is often *on by default* — you opt out in settings, and one provider's 2026 policy still allows training on conversations flagged for safety review. Read the setting, not the marketing. |   
| **Confidential or regulated data** | The only clean answer for client files, health data, anything under a contract. | Possible with a business plan and a data-processing agreement; many organisations forbid it for personal information. |   
| **Canadian public bodies** (a university, a health authority) | Simplest way to satisfy privacy law. | BC's FIPPA *used to* require personal data to stay in Canada; that rule was repealed in November 2021 and replaced by a duty to assess sensitive data. Where the data sits is still not who can be  *compelled* to hand it over (the US CLOUD Act reaches US-headquartered providers). |   
| **Canadian private business** (where most of you will work) | The same clean answer, and the easiest one to defend to a client. | **BC's PIPA** governs provincially regulated private organisations here — it was declared *substantially similar* to the federal **PIPEDA**, which still applies to personal information crossing a provincial or national border and to federally regulated businesses (banks, telecoms, transport). Both want a stated purpose, consent, and safeguards that match how sensitive the data is. None of those is satisfied by "we pasted it into a chat". |   
| **Security of the model itself** | You are the security team: no safety classifiers unless you add them, and a downloaded model file is software — check its source (a Hugging Face model card with a real author beats a random upload). | The provider runs safety systems, patches, and abuse detection — and is also the single big target, and can change terms, prices, or shut a model off. |   
| **Prompt injection / excessive agency** (week 5) | Same risk if you give a local agent tools; nothing about "local" makes an agent obedient. | Same risk; the provider's classifiers catch *some* attacks, and you cannot see which. |   
| **Capability** | Small open models: excellent for private, plentiful, routine work; weaker on hard reasoning and recent facts; a 4,096-token window by default. | The best reasoning available, tools, web access, million-token windows. |   
| **Cost** | Hardware you already own; electricity (a gaming PC at full load ~ $30/month if used 8 hours a day; a laptop, a few dollars). | Cents per conversation; dollars per long one (week 3's table); a subscription for the chat app. |   
| **Energy and ethics** | Per query, a shared datacenter is several times more efficient than your one machine (batching) — but your machine draws nothing when idle and trains nothing. | Training frontier models costs hundreds of megawatts; datacenter siting, water and grid impact are live public debates; so are training-data consent, copyright, and the labour behind RLHF. |   
| **Availability** | Works on a plane, in a lab with no network, during an outage. | Needs the network and the provider to be up. |   
| **Who is accountable** | You. | A contract, if you have one; a policy page, if you do not. |   
   
**The honest rule:** *local for private and plentiful, hosted for hard and*  
 *  
 rare* — and read the training setting on any consumer app you use, this  
   
 week, because it changed in 2025 and it may change again.  
**The rule for this course:** nothing private goes to a hosted model in the  
   
 labs; the week-1 access log and every starter file are synthetic on purpose  
   
 so they can go anywhere.  
*Sources, for the curious:* providers' own data-usage pages (OpenAI, "How  
   
 your data is used to improve model performance"; Anthropic's consumer  
   
 privacy policy, updated 2025–26); BC OIPC on data residency after the 2021  
   
 FIPPA amendment; the Office of the Privacy Commissioner of Canada on the  
   
 provincial laws that apply instead of PIPEDA (BC PIPA, checked 2026-09-14);  
   
 the 2026 local-vs-cloud energy comparisons cited in  
   
 instructor/course-ideas.md.  
**The three policies — read before you sign (checked 2026-09-12, re-checked 2026-10-02)**  
Your assigned model is a hosted web chat run by a company. Its privacy  
   
 policy is the contract. Ten minutes with the right one, before the account  
   
 exists, is Part 3's step 0. What each said on the day this was written —  
   
 **read the current page yourself; policies change, and the date matters:**  
| | | | |  
|-|-|-|-|  
|   | **Kimi K3** ** — kimi.com (K3.1 if it has shipped)** | **DeepSeek V4.1 Flash** ** — chat.deepseek.com (since 10 Sep 2026)** | **GLM-5.3** ** — chat.z.ai (pick it; the default is GLM-5.3-Flash)** |   
| Policy | kimi.com/user/agreement/userPrivacy?version=v2 — the current one, in Chinese with an English translation. **The same address without ** **?version=v2** ** shows a 2024 version.** Signing up from outside China may show a third, international policy (Moonshot AI Pte. Ltd., Singapore, July 2025: trains on content, no opt-out, no storage country named).  **Write down which one you got** | cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html | chat.z.ai/legal-agreement/privacy-policy |   
| Who controls the data | Beijing Moonshot Technology Co., Ltd. (China) in the current policy; the international policy and the API platform name Moonshot AI Pte. Ltd., Singapore | Hangzhou DeepSeek Artificial Intelligence Co., Ltd. (China) | Jingsheng Hengxing Technology Pte. Ltd. (Singapore) |   
| Where it is stored | "within the territory of the People's Republic of China"; no transfer abroad without separate consent | "we directly collect, process and store your Personal Data in People's Republic of China" | "generally processed in Singapore"; may be transferred outside your jurisdiction |   
| Your text used for training? | Yes; you can ask customer service to stop (identity verified first) | Yes — "training and improving … our machine learning models"; a stated right to opt out | Yes — "when we train and improve our models"; no opt-out stated |   
| How long chats are kept | "only as long as necessary for the service" — no number | "as long as you have an account" — no number for chats | Not stated for chats; the business DPA says content is processed in real time and not stored |   
| Deleting | Individual chats in settings; account deletion in settings — irreversible | Chats via settings; account deletion — irreversible, content gone | Individual conversations; account deletion — irreversible |   
| Policy date | Effective 31 Aug 2026 (updated 24 Aug) | Last update 10 Feb 2026 | Last update 29 Sep 2025 |   
   
Two things to notice. First, **the model and the service are different**  
 **  
 things**: the weights of all three are published on Hugging Face under open  
   
 licences (MIT for DeepSeek V4 and GLM-5.3 except its newest release; a  
   
 custom licence for Kimi K3), so a company in Canada could serve the very  
   
 same model under Canadian terms — what you are agreeing to here is the  
   
 *service*, not the model. Second, **the sign-up form is where the choice**  
 **  
 is made** — an email or Google login, sometimes a phone number. Nothing in  
   
 this lab needs anything private typed into any of them; the six prompts  
   
 are public text.  
**A model can carry its maker's rules with it.** China's rules for  
   
 generative-AI services, in force since August 2023, require providers to  
   
 uphold "core socialist values". Running open weights on your own machine  
   
 removes the *service* — its filters, its logs, its terms — but not the  
   
 *training*: what the model was taught to say and not say comes with the  
   
 file. Prompt P6 tests exactly that, on the hosted chats and on your  
   
 desktop.  
**What a policy cannot tell you (added 2 October 2026).** On 10 September  
   
 Anthropic published a report saying that Moonshot had relayed real Kimi  
   
 users' requests to Claude through 5,380 fraudulent accounts — nearly  
   
 300,000 of them in one ten-day stretch, more than 23 million between May  
   
 and July — and shown the answers as Kimi's own, and that DeepSeek had  
   
 relayed about 12 million in two weeks of July. On 23 September China's  
   
 internet regulator was reported to have opened an investigation into both  
   
 companies over what user data had left the country. The accuser is a  
   
 competitor and the probe is not finished, so hold the numbers loosely. The  
   
 shape is the lesson of step 0: **your text can go somewhere the policy**  
 **  
 never named**, and the only text that cannot is the text that never left  
   
 your machine. The regulator's question — whose data went where — is the  
   
 same one your table asks.  
**Route P — you would rather not.** No reason needed, and nobody in this  
   
 course has to sign up for any of these services or give a payment card.  
   
 Ask your instructor to run the six prompts for you with their Kimi or  
   
 DeepSeek account. You get back a file with every answer, how long each  
   
 took, and the model ID the service reported; you check and score them  
   
 exactly as everyone else does. Notice what that changes in step 0: the  
   
 instructor's account is an **API** account, under the developer platform's  
   
 terms rather than the consumer chat's — a different contract for the same  
   
 model, which is the point of this page. The marks are for the checking,  
   
 not the account.  
