Published
Mar 5, 2025
Reading time
13 min read
Published
[Mar 05, 2025](https://www.deeplearning.ai/the-batch/tag/mar-05-2025/)
Reading time
13 min read
Share
Dear friends,
Continuing our discussion on the [Voice Stack](https://www.deeplearning.ai/the-batch/what-ive-learned-building-voice-applications/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--BbTbTGXwD9i_GzQv74w6VjOOwhZ1W4kRbU9GwFHQ6Fdz2XlQj6VMu3t1DzPbLAE4ceL9M), I’d like to explore an area that today’s voice-based systems mostly struggle with: Voice Activity Detection (VAD) and the turn-taking paradigm of communication.
When communicating with a text-based chatbot, the turns are clear: You write something, then the bot does, then you do, and so on. The success of text-based chatbots with clear turn-taking has influenced the design of voice-based bots, most of which also use the turn-taking paradigm.
A key part of building such a system is a VAD component to detect when the user is talking. This allows our software to take the parts of the audio stream in which the user is saying something and pass that to the model for the user’s turn. It also supports interruption in a limited way, whereby if a user insistently interrupts the AI system while it is talking, eventually the VAD system will realize the user is talking, shut off the AI’s output, and let the user take a turn. This works reasonably well in quiet environments.
However, VAD systems today struggle with noisy environments, particularly when the background noise is from other human speech. For example, if you are in a noisy cafe speaking with a voice chatbot, VAD — which is usually trained to detect human speech — tends to be inaccurate at figuring out when you, or someone else, is talking. (In comparison, it works much better if you are in a noisy vehicle, since the background noise is more clearly not human speech.) It might think you are interrupting when it was merely someone in the background speaking, or fail to recognize that you’ve stopped talking. This is why today’s speech applications often struggle in noisy environments.
![Diagram of an RQ-Transformer speech system with Helium Temporal Transformer, Depth Transformer, Mimi, and Moshi for audio processing.](https://dl-staging-website.ghost.io/content/images/2025/03/unnamed--56-.png)
Intriguingly, last year, Kyutai Labs published [Moshi](https://www.deeplearning.ai/the-batch/moshi-an-open-alternative-to-openais-realtime-api-for-speech/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--BbTbTGXwD9i_GzQv74w6VjOOwhZ1W4kRbU9GwFHQ6Fdz2XlQj6VMu3t1DzPbLAE4ceL9M), a model () that had many technical innovations. An important one was enabling persistent bi-direction audio streams from the user to Moshi and from Moshi to the user.
If you and I were speaking in person or on the phone, we would constantly be streaming audio to each other (through the air or the phone system), and we’d use social cues to know when to listen and how to politely interrupt if one of us felt the need. Thus, the streams would not need to explicitly model turn-taking. Moshi works like this. It’s listening all the time, and it’s up to the model to decide when to stay silent and when to talk. This means an explicit VAD step is no longer necessary. (Moshi also included other innovations, such as an “inner monologue” that simultaneously generates text alongside the audio to improve the quality of responses as well as audio encoding.)
Just as the architecture of text-only transformers has gone through many evolutions (such as encoder-decoder models, decoder-only models, and reasoning models that generate a lot of “reasoning tokens” before the final output), voice models are going through a lot of architecture explorations. Given the importance of foundation models with voice-in and voice-out capabilities, many large companies right now are investing in developing better voice models. I’m confident we’ll see many more good voice models released this year.
It feels like the space of potential innovation for voice remains large. Hard technical problems, like the one of latency that I described last week and VAD errors, remain to be solved. As solutions get better, voice-to-voice will continue to be a promising category to build applications in.
Keep building!
Andrew

## A MESSAGE FROM DEEPLEARNING.AI

[![Promo banner for: "Event-Driven Agentic Document Workflows"](https://dl-staging-website.ghost.io/content/images/2025/03/The-Batch-ads-and-exclusive-banners---2025-03-03T153624.042.png)](https://www.deeplearning.ai/short-courses/event-driven-agentic-document-workflows/?ref=dl-staging-website.ghost.io)
Learn to build an event-driven AI agent that processes documents and fills out forms using RAG, workflows, and human-in-the-loop feedback. This course, built in partnership with LlamaIndex, walks you through designing, building, and refining automated document workflows. [Enroll for free](https://www.deeplearning.ai/short-courses/event-driven-agentic-document-workflows/?ref=dl-staging-website.ghost.io)

# News

![Table evaluating Mercury Coder Mini, Mercury Coder Small, Gemini 2.0 Flash-Lite, Claude 3.5 Haiku, GPT-4o Mini, Qwen 2.5 Coder 7B, and DeepSeek Coder V2 Lite for throughput, HumanEval, MBPP, EvalPlus, MultiPL-E, and code completion.](https://dl-staging-website.ghost.io/content/images/2025/03/unnamed--57-.png)

# Text Generation by Diffusion

Typical large language models are autoregressive, predicting the next token, one at a time, from left to right. A new model hones all text tokens at once.
**What’s new:** Inception Labs, a Silicon Valley startup, emerged from stealth mode with [Mercury Coder](https://info.deeplearning.ai/e3t/Ctc/LX+113/cJhC404/VW1BHQ7gMz_KW23Xl7-31VLBlVBzM2_5sPFbBN3cFw5H3qgyTW6N1vHY6lZ3kNN6r7zGkSml0mW7_y59p40R9P6W5QSKFV7tGBlMW5LBV6G86YdNhW96pM3V5fYbqmW5rGDj522hFfFW8KYyM12zfX9JW3mY5fJ5WJbCJW6PGltX6NRfK8W7PVCX81qYcR5W4K34wL4Djk8TW5CX6Q95VMH6FW39wPQf6Bm36TW5C0cSS48bVL9W6MM4gm8x--fkW87_tjN5pq-dWVGYMJj8hLNHdW42nQjn6lXyZJW8Fp0ZQ2Z7WJFF5D-Sltbk1hN2Qkx1vMRgHMW67MKqM57HCW3f7mLbMW04?ref=dl-staging-website.ghost.io), a diffusion model that generates code, in small and mini versions. Registered users can try it out [here](https://info.deeplearning.ai/e3t/Ctc/LX+113/cJhC404/VW1BHQ7gMz_KW23Xl7-31VLBlVBzM2_5sPFbBN3cFw5H3qgyTW6N1vHY6lZ3lfW468kdf5ps3DjVptPX56Kv07RV_xtY-4k8D41W1Rnkzb6GnPxRW3kKcpC4k63S0W1BKTnl4rpwXDW6ybHxs9cP8jRW4fdRGZ5TS-HgW8hlRGq3_B092W8lzgWR90JwHcVgZLkj5VvjJvW7pcd3h83ChccW3CmNn82kBQNCW96QNsC3cKjvqW5VZmq613THQnW6zv7TJ4dRPN-W3MmmfV6-M2rdW12vX2x42BB33W3gQxMY3lHnbXW42jCQ0421BJdN318zPJ7rp6nN2LT0dsJpvLhf3FYW_F04?ref=dl-staging-website.ghost.io), and an API (sign up for early access [here](https://info.deeplearning.ai/e3t/Ctc/LX+113/cJhC404/VW1BHQ7gMz_KW23Xl7-31VLBlVBzM2_5sPFbBN3cFw5H3qgyTW6N1vHY6lZ3lXW5Z940V56zqXQW56_hck41PG_qW3MRdw685ly7yW647dDG6Xr0y3W1dj_bN5H938BW6532yz5Pvys0W5SfP9T8B93PnW3y_3b13HPwTmW4rsdvD32_P2qW3LF4pt2fmBlvN9dh9WtnDNmPW6Fxf1097nGnFVF7_w080XD0VW3QP-JK5q4YNfW1RjyHL16bd9bW6NTFxy6NBfGxW4lnDlZ3M80nLW8SvG_z1s1NlcW516tVS7TRXYYW6R1_Wf92DzkcW5ZRx2r1HpdKvW4Csw0T34z-Wwf5y9P9P04?ref=dl-staging-website.ghost.io)) and on-premises deployments are in the works. The company has not yet announced availability and pricing.
**How it works:** Like image diffusion models, Mercury Coder improves its output over a number of steps by removing noise.

- Inception Labs shared little information about the model, leaving details including parameter count, input size and output size, training data, and training methods undisclosed.
- An October 2023 [paper](https://info.deeplearning.ai/e3t/Ctc/LX+113/cJhC404/VW1BHQ7gMz_KW23Xl7-31VLBlVBzM2_5sPFbBN3cFw5H3qgyTW6N1vHY6lZ3nbVxP5St6g0BBbW9bLy0M2QZTlVW5tm_Ws7V348mW3GfrVy8PFXDCN5rK9bQGJGDCN1bYs_hpcQbFVvn2LP4yQN8ZW82kSGb4lX8yLW6Twh7M3qX_MxW5CqP1y3FYWnxW76cNhf2n_lg-W36qD9j7FgrSLW7VmwBp2DT9NBW68TR6y2XC2JxMNFs-BDHqn-W4PdQCm1VxdBpW62wFSR1ch_blW6Gx16S3rnQbzW1PRGNK7wt83wW4sNrjy2w67jlW9hFhJ-7X3w0pW55ljJl4VnSl4f3mZPv404?ref=dl-staging-website.ghost.io) co-authored by an Inception Labs co-founder describes training a text diffusion model using score entropy. The model learned to estimate the transition ratio between two tokens; that is, the probability that token y is correct over the probability that the current token x is correct.
- In their most successful experiments, the authors added noise to tokens by progressively masking an ever-greater percentage of tokens at random over several steps.
- At inference, the model started with masked tokens and unmasked them over a number of steps. The estimated transition ratio determined how to change each token at each step.

**Results:** Mercury Coder’s major advantage is speed, but it also performs well compared to several competitors.

- The Small and Mini versions are 3.5 to 18 times faster than comparable small coding models. Running on an Nvidia H100 graphics processing unit, Mercury Coder Small generates 737 tokens per second and Mercury Coder Mini generates 1,109 tokens per second. In comparison, Qwen 2.5 Coder 7B generates 207 tokens per second and GPT 4o-Mini generates 59 tokens per second.
- On coding tasks across six benchmarks, Mercury Coder Small outperforms Gemini 2.0 Flash-Lite, Claude 3.5 Haiku, GPT-4o Mini, and Qwen 2.5 Coder 7B on at least four. Mercury Coder Mini beats those models on at least two. Both versions of Mercury Coder lost to DeepSeek Coder V2 Lite on all six benchmarks.

**Behind the news:** Several teams have built diffusion models that generate text, but previous efforts have not been competitive with autoregressive large language models (LLMs). Recently, [LLaDA](https://info.deeplearning.ai/e3t/Ctc/LX+113/cJhC404/VW1BHQ7gMz_KW23Xl7-31VLBlVBzM2_5sPFbBN3cFw5H3qgyTW6N1vHY6lZ3kzW8Y-6-z1NHlGkW29NvFC4sM43NW62QBVX6DcbfdW3v8gFQ4gCFwqW4q5Qmn3LyGSCW2d8h7N5mNLlnW6L8hVT2mrJSXN2shXb8KZcb9W1Tzfh92tbpvSW94DQPM42qstCW23Hys16nPv1vN69CPJFM27-tW55rbdt2YpVLKW6jYrch6W6jhfW92rP5_66rfc_W64z3TV4XZJS4W65VMfT7y6Qs0W6bLXN926k03fW2Xm_wL9g_B7rW75CKBk5gj460W2ZkRTk64qyW7Vbrr0P3HG6w5f217Zk604?ref=dl-staging-website.ghost.io) showed comparable performance to Meta’s Llama 2 7B but fell short of Llama 3 8B and other similarly sized modern LLMs.
**Why it matters:** Text diffusion models are already faster than autoregressive models. They offer significant promise to accelerate text generation even further.
**We’re thinking:** Diffusion image generators have delivered good output with as little as four or even one step, generating output tokens significantly faster than autoregressive models. If text diffusion models can benefit from improvements in image generation, they could lead to rapid generation of lengthy texts and, in turn, faster agents and reasoning.
![Table comparing GPT-4.5, GPT-4o, and OpenAI o3-mini across benchmarks including GPQA, AIME 2024, MMLU, MMMU, and various coding tests.](https://dl-staging-website.ghost.io/content/images/2025/03/unnamed--58-.png)

# OpenAI’s GPT-4.5 Goes Big

OpenAI launched GPT-4.5, which may be its last non-reasoning model.
**What’s new:** GPT-4.5 is as a research preview. Unlike OpenAI’s recent models o1 and o3, GPT-4.5 is not fine-tuned to reason by generating a chain of thought, although the company hinted that it may serve as a basis of a reasoning model in the future. Instead, it’s a huge model that was trained using a huge amount of computation. As OpenAI’s biggest model to date, GPT-4.5 is to run, and the company is evaluating whether to offer it via API in the long term.

- **Input/output:** text and images in, text out. Voice and video interactions may be available in future updates.
- **Availability/price:** Via ChatGPT (currently ChatGPT Pro; soon ChatGPT Plus, Team, Enterprise, and Edu) and various APIs (Chat Completions, Assistants, and Batch). $75/$150 per million input/output tokens.
- **Features:** Web search, function calling, structured output, streaming, system messages, [canvas](https://www.deeplearning.ai/short-courses/collaborative-writing-and-coding-with-openai-canvas/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--BbTbTGXwD9i_GzQv74w6VjOOwhZ1W4kRbU9GwFHQ6Fdz2XlQj6VMu3t1DzPbLAE4ceL9M) collaborative user interface.
- **Undisclosed:** Parameter count, input and output size, architecture, training data, training methods.

**How it works:** OpenAI revealed few about how GPT-4.5 was built. The model is bigger than GPT-4o, and it was pretrained and fine-tuned on more data using more computation — possibly 10x more, given OpenAI’s comment that “with every new order of magnitude of compute comes novel capabilities.”

- The model was trained on a combination of publicly available data and data from partnerships and in-house datasets, including data generated by smaller models. Its knowledge cutoff is October 2023.
- The data was filtered for quality, to eliminate personally identifying information, and to eliminate information that might contribute to proliferation of chemical, biological, radiological, and nuclear threats.
- OpenAI developed unspecified techniques to scale up unsupervised pretraining, supervised fine-tuning, and alignment.

**Performance:** “This isn’t a reasoning model and won’t crush benchmarks,” OpenAI CEO Sam Altman warned in a . The company claims that GPT-4.5 offers improved general knowledge, adheres to prompts with more nuance, delivers greater creativity, and has higher emotional intelligence.

- GPT-4.5 shows less propensity to hallucinate, or confabulate information, than other OpenAI models. On PersonQA (questions that involve publicly available facts about people), GPT-4.5 achieved 78 percent accuracy compared to GPT-4o (28 percent accuracy) and o1 (55 percent accuracy). Moreover, GPT-4.5 achieved a hallucination rate (lower is better) of 0.19 compared to GPT-4o (0.52) and o1 (0.20).
- Its performance on coding benchmarks is mixed. On , GPT-4.5 achieved a 38 percent pass rate, higher than GPT-4o (30.7 percent) but well below [deep research](https://www.deeplearning.ai/the-batch/openais-deep-research-agent-generates-detailed-reports-by-analyzing-web-sources/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--BbTbTGXwD9i_GzQv74w6VjOOwhZ1W4kRbU9GwFHQ6Fdz2XlQj6VMu3t1DzPbLAE4ceL9M) (61 percent), an agentic workflow that conducts multi-step research on the internet. On , which evaluates full-stack software engineering tasks, GPT-4.5 solved 32.6 percent of tasks, outperforming GPT-4o (23.3 percent) and o3-mini (10.8 percent) but again lagging deep research (around 48 percent).

**Behind the news:** GPT-4.5’s release comes as OpenAI nears an announced away from developing separate general-knowledge and reasoning models. The launch also comes as OpenAI faces an ongoing shortage of processing power. CEO Sam Altman that the company is “out of GPUs” and struggling to meet demand — a constraint that may impact whether OpenAI continues to offer GPT-4.5 via API.
**Why it matters:** GPT-4.5 highlights a growing divide in AI research over whether to pursue performance gains by scaling up processing during pretraining or inference. Despite the success of approaches that consume extra processing power at inference, such as agentic techniques and reasoning models such as its own o family, OpenAI clearly still sees value in pretraining larger and larger models.
**We’re thinking:** There’s still more juice to be squeezed out of bigger models! We’re excited to see what the combination of additional compute applied to both pretraining and inference can achieve.
![Table comparing Claude 3.7 Sonnet, 3.5 Sonnet, o1, o3-mini, DeepSeek R1, and Grok 3 Beta on graduate-level reasoning, coding, tool use, visual reasoning, instruction following, and high school math competition performance.](https://dl-staging-website.ghost.io/content/images/2025/03/unnamed--59-.png)

# Budget for Reasoning to the Token

Anthropic’s Claude 3.7 Sonnet implements a hybrid reasoning approach that lets users decide how much thinking they want the model to do before it renders a response.
**What’s new:** was trained for strong performance in coding and front-end web development, with less emphasis on math and computer-science competition problems. It implements tool use and computer use (but not web search) and lets users toggle between immediate responses and , which can improve outputs by allocating a specific number of tokens to reasoning at inference. Like DeepSeek-R1 and Google Gemini Flash Thinking — and unlike OpenAI o1 — Claude 3.7 Sonnet fully displays reasoning tokens. Anthropic considers this functionality experimental, so it may change.

- **Input/output:** text and images in (up to 200,000 tokens), text out (up to 128,000 tokens).
- **Availability/price:** Via Anthropic tiers Free (extended thinking not available), Pro, Team, and Enterprise; Anthropic API; Amazon Bedrock; Google Cloud Vertex AI. $3/$15/$15 per million input/output/thinking tokens.
- **Undisclosed:** parameter count, architecture, training data, training method.
- Anthropic also introduced Claude Code, a command-line tool for AI-assisted coding, which is available as a limited research preview. Claude Code can edit files, write and run tests, commit and push code to GitHub, and use command-line tools.

**How it works:** Anthropic pretrained Claude 3.7 Sonnet on a mix of public and proprietary data (which explicitly did not include Claude users’ inputs and outputs). The team fine-tuned Claude 3.7 Sonnet using [constitutional AI](https://www.deeplearning.ai/the-batch/toward-safer-more-helpful-models/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--BbTbTGXwD9i_GzQv74w6VjOOwhZ1W4kRbU9GwFHQ6Fdz2XlQj6VMu3t1DzPbLAE4ceL9M), which encourages a model to follow a set of human-crafted rules.

- When the model’s extended thinking mode is enabled, API users can control the thinking budget by specifying a number of tokens up to 128,000. (The specified budget is a rough target, so the number of tokens consumed may differ.)
- Anthropic says that extended thinking mode often is more effective given a general instruction to “think deeply” rather than step-by-step instructions.
- Visible thinking tokens are considered a research preview while Anthropic examines how they affect user interactions with the model. The company highlights three issues: Visible thinking tokens don’t reflect the model’s internal instructions that establish its character and therefore seem to be devoid of personality, they may not reflect the model’s actual reasoning process, and they can reveal flaws that malicious actors may exploit.
- Extended thinking mode processes tokens serially, but Anthropic is experimenting with parallel thinking that follows multiple independent thought processes and chooses the best one according to a majority vote.

**Performance:** Claude 3.7 Sonnet shows exceptional performance in general knowledge, software engineering, and agentic tasks.

- On the (graduate-level science questions), Claude 3.7 Sonnet achieved 84.8 percent in parallel extended thinking mode with a 64,000-token budget. By comparison, X’s Grok 3 beta achieved 84.6 percent (majority voting with 64 tries), and OpenAI’s o3-mini achieved 79.7 percent with high effort.
- On , which evaluates the ability to solve real-world software engineering problems, Claude 3.7 Sonnet achieved 70.3 percent without extended thinking, averaged over 16 trials. OpenAI’s o3-mini achieved 49.3 percent with high effort, and DeepSeek R1 achieved 49.2 percent with extended thinking, 32,000 tokens.
- TAU-bench evaluates agentic reasoning. On the Retail subset, which assesses performance in product recommendations and customer service, Claude 3.7 Sonnet achieved 81.2 percent without extended thinking, outperforming OpenAI’s o1 (73.5 percent). In the Airline subset, which measures multi-step reasoning in tasks like flight bookings and customer support, Claude 3.7 Sonnet achieved 58.4 percent, likewise ahead of o1 (54.2 percent).
- On , competitive high-school math problems, Claude 3.7 Sonnet achieved 80.0 percent in parallel extended thinking mode with a 64,000-token budget. In this test, it underperformed o3-mini with high effort (87.3 percent) and o1 (83.3 percent).

**Behind the news:** Anthropic’s approach refines earlier efforts to enable users to control the incremental expense of computing extra tokens at inference. For instance, OpenAI o1 offers three levels of reasoning or “effort” — each of which allocates more tokens to reasoning — while X’s [Grok 3](https://www.deeplearning.ai/the-batch/grok-3-xais-new-model-family-improves-on-its-predecessors-adds-reasoning/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--BbTbTGXwD9i_GzQv74w6VjOOwhZ1W4kRbU9GwFHQ6Fdz2XlQj6VMu3t1DzPbLAE4ceL9M) offers two.
**Why it matters:** , or additional processing at inference, is powerful but expensive, and not all tasks benefit from it. So it’s helpful to let users choose how much to apply. Claude 3.7 Sonnet improves its predecessor’s general performance and provides an ample budget for additional reasoning.
**We’re thinking:** The cost of inference is rising as agentic workflows and other compute-intensive tasks become more widely used. Yet the cost of AI on a per-token basis is [falling](https://www.deeplearning.ai/the-batch/falling-llm-token-prices-and-what-they-mean-for-ai-companies/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--BbTbTGXwD9i_GzQv74w6VjOOwhZ1W4kRbU9GwFHQ6Fdz2XlQj6VMu3t1DzPbLAE4ceL9M) rapidly. Intelligence is becoming steadily cheaper and more plentiful.
![Amazon smart display featuring widgets for recommended recipes, calendar, weather, daily events, and streaming services like Prime Video, Netflix, and Disney+.](https://dl-staging-website.ghost.io/content/images/2025/03/unnamed--52-.gif)

# Amazon’s Next-Gen Voice Assistant

Amazon announced Alexa+, a major upgrade to its long-running voice assistant.
**What’s new:** , which accepts spoken commands and responds conversationally, is designed to work with a variety of vendors as an autonomous agent to make purchases, book reservations, play media, and so on. It will roll out in the U.S. over coming weeks, initially on some Echo Show devices and eventually nearly every current Echo speaker.
**How it works:** Alexa+ the system to take advantage of generative AI including Anthropic Claude, [Amazon Nova](https://www.deeplearning.ai/the-batch/amazon-introduces-nova-models-for-text-image-and-video/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--BbTbTGXwD9i_GzQv74w6VjOOwhZ1W4kRbU9GwFHQ6Fdz2XlQj6VMu3t1DzPbLAE4ceL9M), and other large language models. Inputs are filtered through a routing system that determines the best model to respond to any given request. It’s trained to understand colloquial, conversational language. Its personality is designed to be “smart, considerate, empathetic, and inclusive” as well as humorous.

- Alexa+ interacts with online vendors to manage smart-home devices (Philips Hue, Ring, Roborock), reserve restaurant seats (OpenTable, Vagaro), play music (Amazon Music, Spotify, Apple Music, iHeartRadio) and videos (Amazon Video, Hulu, Netflix, Disney+), book local service technicians (Thumbtack), and purchase items (Amazon Fresh, Whole Foods, Grubhub, Uber Eats, Ticketmaster). Amazon+ will cost $19.99 per month, free with an Amazon Prime membership ($139 per year). (Disclosure: Andrew Ng is a member of Amazon’s board of directors.)
- The system recognizes individual users and keeps track of personalized information such as dates; recipes, and preferences in sports, food, music, and movies. In addition, it can respond to queries based on purchase records, video and music playbacks, shipping addresses, documents, emails, photos, messages, and so on.
- It can behave proactively, for instance, advising users to start their commute early if traffic is heavy.
- The system calls what Amazon calls experts — groups of systems, APIs, and instructions — that orchestrate API calls to accomplish online tasks. For instance, it can navigate and use the web to perform tasks such as finding and booking, say, a local repair service to fix a broken household appliance.
- Alexa+ can deliver timely news and information based on partnerships with news sources including _Associated Press_ , _Business Insider_ , _Politico_ , _Reuters_ , _USA Today_ , and _The Washington Post_.

**Behind the news:** Amazon launched Alexa in 2014, and the voice assistant now resides in over 600 million devices worldwide. However, users relied on it more to set timers, report sports scores, and play music than to purchase products, and Alexa revenue lagged. Following cutbacks in 2021, Amazon made [multibillion-dollar](https://www.deeplearning.ai/the-batch/anthropic-secures-2-billion-investment-from-google-weeks-after-amazon-deal/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--BbTbTGXwD9i_GzQv74w6VjOOwhZ1W4kRbU9GwFHQ6Fdz2XlQj6VMu3t1DzPbLAE4ceL9M) [investments](https://www.deeplearning.ai/the-batch/amazon-deepens-anthropic-partnership-with-4-billion-investment/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--BbTbTGXwD9i_GzQv74w6VjOOwhZ1W4kRbU9GwFHQ6Fdz2XlQj6VMu3t1DzPbLAE4ceL9M) in Anthropic and set about updating the technology for the generative AI era.
**Why it matters:** Alexa, along with Apple’s Siri and Google Assistant, pioneered the market for voice assistants. However, as large language models (LLMs) blossomed, all three systems fell behind the times. (Google allows Android users to substitute one of its Gemini LLMs for Google Assistant, but the system still calls Google Assistant for some tasks.) Alexa+ is the first major voice-assistant update that aims to take advantage of LLMs as well as emerging agentic technology and improved voice interactions, and the rollout is taking these capabilities to a large, existing user base.
**We’re thinking:** Rapid improvements in the [voice stack](https://www.deeplearning.ai/the-batch/issue-290/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--BbTbTGXwD9i_GzQv74w6VjOOwhZ1W4kRbU9GwFHQ6Fdz2XlQj6VMu3t1DzPbLAE4ceL9M) are opening doors not only for voice assistants but for a galaxy of applications that rely on spoken input and output. Product designers will need to learn how to design smooth user voice experiences. Watching how Alexa+ manages them will provide useful guidelines.
![Generative AI for Everyone](https://www.deeplearning.ai/_next/image/?url=https%3A%2F%2Fhome-wordpress.deeplearning.ai%2Fwp-content%2Fuploads%2F2023%2F10%2FGenAI4E_sidebanner.png&w=3840&q=75)
Share

## Subscribe to The Batch

Stay updated with weekly AI News and Insights delivered to your inbox
Email\*

- Keep me updated on the latest news, courses, and workshops and events announcements

- [Courses](https://www.deeplearning.ai/courses/)
- [The Batch](https://www.deeplearning.ai/the-batch/)
- [Community](https://www.deeplearning.ai/community/)
- [Careers](https://www.deeplearning.ai/careers/)
- [About](https://www.deeplearning.ai/about/)
