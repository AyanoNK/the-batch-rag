Published
Apr 23, 2025
Reading time
12 min read
Published
[Apr 23, 2025](https://www.deeplearning.ai/the-batch/tag/apr-23-2025/)
Reading time
12 min read
Share
Dear friends,
Even though I’m a much better Python than JavaScript developer, with AI assistance, I’ve been writing a lot of JavaScript code recently. AI-assisted coding is making specific programming languages less important, even though learning one is still helpful to make sure you understand the key concepts. This is helping many developers write code in languages we’re not familiar with, which lets us get code working in many more contexts!
My background is in machine learning engineering and back-end development, but AI-assisted coding is making it easy for me to build front-end systems (the part of a website or app that users interact with) using JavaScript (JS) or TypeScript (TS), languages that I am weak in. Generative AI is making syntax less important, so we can all simultaneously be Python, JS, TS, C++, Java, and even Cobol developers. Perhaps one day, instead of being “Python developers" or “C++ developers,” many more of us will just be “developers”!
But understanding the concepts behind different languages is still important. That’s why learning at least one language like Python still offers a great foundation for prompting LLMs to generate code in Python and other languages. If you move from one programming language to another that carries out similar tasks but with different syntax — say, from JS to TS, or C++ to Java, or Rust to Go — once you’ve learned the first set of concepts, you’ll know a lot of the concepts needed to prompt an LLM to code in the second language. (Although TensorFlow and PyTorch are not programming languages, learning the concepts of deep learning behind TensorFlow will also make it much easier to get an LLM to write PyTorch code for you, and vice versa!) In addition, you’ll be able to understand much of the generated code (perhaps with a little LLM assistance).
![Code snippet showing ‘Keep Building!’ printed in multiple programming languages including Python, Java, JavaScript, and C++.](https://dl-staging-website.ghost.io/content/images/2025/04/unnamed--61--1.jpg)
Different programming languages reflect different views of how to organize computation, and understanding the concepts is still important. For example, someone who does not understand arrays, dictionaries, caches, and memory will be less effective at getting an LLM to write code in most languages.
Similarly, a Python developer who moves toward doing more front-end programming with JS would benefit from learning the concepts behind front-end systems. For example, if you want an LLM to build a front end using the React framework, it will benefit you to understand how React breaks front ends into reusable UI components, and how it updates the DOM data structure that determines what web pages look like. This lets you prompt the LLM much more precisely, and helps you understand how to fix issues if something goes wrong. Similarly, if you want an LLM to help you write code in CUDA or ROCm, it helps to understand how GPUs organize compute and memory.
Just as people who are fluent in multiple human languages can communicate more easily with other people, LLMs are making it easier for developers to build systems in multiple contexts. If you haven’t already done so, I encourage you to try having an LLM write some code in a language you’d like to learn but perhaps haven’t yet gotten around to, and see if it helps you get some new applications to work.
Keep building!
Andrew

## A MESSAGE FROM DEEPLEARNING.AI

[![Promo banner for "Building Code Agents with Hugging Face smolagents"](https://dl-staging-website.ghost.io/content/images/2025/04/The-Batch-ads-and-exclusive-banners---2025-04-23T105320.680.png)](https://www.deeplearning.ai/short-courses/building-code-agents-with-hugging-face-smolagents/?ref=dl-staging-website.ghost.io)
Learn to build agents that write and run code to complete complex tasks. “Building Code Agents with Hugging Face smolagents,” made in collaboration with Hugging Face, teaches you how to build code agents, execute their code safely, and set up evals for production-ready multi-agent systems, using the smolagents framework. [Enroll for free](https://www.deeplearning.ai/short-courses/building-code-agents-with-hugging-face-smolagents/?ref=dl-staging-website.ghost.io)

# News

![Comparison chart of GPT-4.1, o3, and o4-mini with other models on coding, math, tool use, and multimodal reasoning benchmarks.](https://dl-staging-website.ghost.io/content/images/2025/04/OpenAI-MODELS_table-11b_1200px.jpg)

# OpenAI Launches Cost-Effective Alternatives

OpenAI refreshed its roster of models and scheduled the largest, most costly one for removal.
**What’s new:** OpenAI introduced five new models that accept text and images inputs and generate text output. Their parameter counts, architectures, training datasets, and training methods are undisclosed. The general-purpose are available via API only. The reasoning models are available via API to developers as well as users of ChatGPT Plus, Pro, and Team, and soon ChatGPT Enterprise and ChatGPT Education. The company will GPT-4.5 — which it introduced as a research preview in late February — in July.
**GPT-4.1 family:** In an odd turn of version numbers, the GPT-4.1 models are intended to be cost-effective equivalents to GPT-4.5 and updates to GPT-4o. They accept inputs of up to 1 million tokens (compared to GPT-4.5’s and GPT-4o’s 128,000 tokens).

- **Prices:** GPT-4.1 $2/$8 per million input/output tokens. GPT-4.1 mini costs $0.40/$1.60 per million input/output tokens. GPT-4.1 nano costs $0.10/$0.40 per million input/output tokens. A 75 percent discount applies to cached input tokens.
- **GPT-4.1 performance:** GPT-4.1 surpassed GPT-4o on most benchmarks tested by OpenAI, with notable improvement on coding tasks. It significantly outperformed GPT-4o, o1, and o3-mini on (real-world coding skills), (following instructions in multi-turn conversations), MMMU (multimodal reasoning), and (long-context understanding).
- **GPT-4.1 mini performance:** The smaller GPT-4.1 mini generally surpassed GPT-4o mini on benchmarks tested by OpenAI. On MultiChallenge and MMMU, GPT-4.1 mini outperformed the full-size GPT-4o.

**o3 and o4-mini:** These models update o1 and o3-mini, respectively. They have input limits of 200,000 tokens and can be set to low-, medium-, or high-effort modes to process varying numbers of reasoning tokens, which are hidden from users. Unlike their predecessors, they were fine-tuned to decide when and how to use the tools, including web search, code generation and execution, and image editing.

- **Prices:** API access to o3 costs $10/$40 per million input/output tokens. o4-mini costs $1.10/$4.40 per million input/output tokens. Both offer a 75 percent discount for cached input tokens.
- **Access limits:** Developers whose usage puts them in rate-limit tiers 1 through 3 must their identities to use o3 via the API (higher-usage tiers 4 and 5 are exempt). OpenAI says this limitation is intended to prevent abuse.
- **Image processing:** o3 and o4-mini can apply chains of thought to images — a first for OpenAI’s reasoning models. For example, users can upload a diagram with instructions to interpret it, and the models will use chains of thought and tools to process the diagram.
- **o3 performance:** o3 set the state of the art in several benchmarks including MultiChallenge, MMMU, MathVista, and HLE. It generally outperformed o1 in tests performed by OpenAI. OpenAI didn’t document o3’s long-context performance, but in independent tests by , it achieved nearly perfect accuracy with contexts up to 120,000 tokens.
- **o4-mini performance:** o4-mini generally outperformed o3-mini in tests performed by OpenAI. It outperformed most competing models in Fiction.Live’s tests of long-context performance.

**Behind the news:** Late last year, OpenAI introduced [o1](https://www.deeplearning.ai/the-batch/openais-o1-models-excel-in-reasoning-outperform-gpt-4o-in-math-and-coding/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj), the first commercial model trained via reinforcement learning to generate chains of thought. Within a few months, DeepSeek, Google, and Anthropic launched their respective reasoning models [DeepSeek-R1](https://www.deeplearning.ai/the-batch/how-deepseek-r1-and-kimi-k1-5-use-reinforcement-learning-to-improve-reasoning/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj), [Gemini 2.5 Pro](https://www.deeplearning.ai/the-batch/googles-gemini-2-0-flash-thinking-advances-in-reasoning-outperforms-deepseek-r1?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj), and [Claude 3.7 Sonnet](https://www.deeplearning.ai/the-batch/claude-3-7-sonnet-introduces-hybrid-reasoning-and-extended-thinking/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj). OpenAI has promised to integrate its general-purpose GPT-series models and o-series reasoning models, but they remain separate for the time being.
**Why it matters:** GPT-4.5 was an exercise in scale, and it showed that continuing to increase parameter counts and training data would yield ongoing performance gains. But it wasn’t widely practical on a cost-per-token basis. The new models, including those that use chains of thought and tools, deliver high performance at lower prices.
**We’re thinking:** Anthropic is one of OpenAI’s key competitors, and a large fraction of the tokens it generates (via API) are for [writing code](https://www.deeplearning.ai/the-batch/anthropic-reveals-how-users-interact-with-claude-3-5?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj), a skill in which it is particularly strong. OpenAI’s emphasis on models that are good at coding could boost the competition in this area!
![Person interacting with a humanoid robot using virtual reality headset and controllers.](https://dl-staging-website.ghost.io/content/images/2025/04/unnamed--78-.png)

# Hugging Face Rolls Out Open Robot

Hugging Face has made a name by providing open AI models. Now it’s providing an open robot.
**What’s new:** Hugging Face the French company Pollen Robotics for an undisclosed price. It plans to offer Pollen’s , a robot that runs on code that’s freely under an Apache 2.0 license, for $70,000.
**How it works:** Reachy 2 has two arms, gripper hands, and a wheeled base (optional). It’s designed primarily for education and research in human-robot interaction in real-world settings.

- Reachy 2 is programmable in Python and runs models from Hugging Face’s library.
- It runs control software locally on a (a PC based on an processor) and processes AI in the cloud or on a local server.
- The robot responds to VR controllers including Meta Quest 2 and 3 as well as Pollen’s VR app.
- Its head senses the visual environment using a pair of cameras equipped with global shutters to capture fast-changing events and measures distances via an optical sensor. Its antennas are outfitted with microphones to capture sounds, and its torso senses distances using a depth camera. The base includes a lidar sensor to aid navigation.
- The body features 3D joints in the neck and wrists and 2D joints in the shoulders and elbows. Each arm can lift objects of up to 3 kilograms.
- A rechargeable, 24 volt battery provides around 10 hours of battery life.

**Behind the news:** Last year, Remi Cadene, who worked on Tesla’s Optimus, Hugging Face to lead robotics projects. In May, he and his team rolled out the LeRobot open source robotics code library, which pretrained models, datasets, and simulators for reinforcement learning and imitation learning. In November, Nvidia announced a with Hugging Face to accelerate LeRobot’s data collection, training, and verification.
**Why it matters:** Hugging Face’s acquisition of Pollen reflects an industry-wide [investment](https://www.deeplearning.ai/the-batch/amazon-strengthens-logistics-and-robotics-with-new-ai-partnership/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj) [in](https://www.deeplearning.ai/the-batch/p0-a-machine-learning-system-for-household-robotics/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj) [robots](https://www.deeplearning.ai/the-batch/unitree-and-engineai-showcase-affordable-humanoid-robots/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj), notably [humanoid](https://www.deeplearning.ai/the-batch/dances-with-robots/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj) robots, whose prices have been [falling](https://www.deeplearning.ai/the-batch/unitree-and-engineai-showcase-affordable-humanoid-robots/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj). Nvidia CEO Jensen Huang has called a “multi-trillion dollar” opportunity.
**We’re thinking:** AI-enabled robots are marching slowly toward what we hope will be breakthrough applications. Open-source systems are an important part of the trend!
![NVIDIA AI computing hardware with multiple GPUs on a black reflective surface.](https://dl-staging-website.ghost.io/content/images/2025/04/unnamed--79-.png)

# U.S. Tightens Grip on AI Chips

The U.S. government escalated its long-running effort to block China’s access to cutting-edge AI hardware.
**What’s new:** The White House that future shipments of Nvidia H20s, AMD MI308s, or equivalent chips to China would require a license. Concurrently, the United States Congress an investigation into whether chip vendor Nvidia violated earlier export rules.
**How it works:** Nvidia launched the H20 in late 2023 to comply with a 2022 U.S. ban on China-bound shipments of Nvidia’s H100 and . The H20 uses the same architecture as the H200, but it’s an order of magnitude slower with less memory and memory bandwidth.

- Nvidia estimated that the new restrictions will the company $5.5 billion in revenue. AMD similarly expects to $800 million.
- Congressional leaders opened an investigation into whether Nvidia assisted DeepSeek with developing AI models, a potential violation of U.S. trade restrictions.
- The action spurred China’s biggest chip maker to accelerate production of its own AI chips. Huawei plans to begin mass shipments of its Ascend 910C AI chip, which is purportedly equivalent to Nvidia’s H100, in May, _Reuters_ . The company expects to mass produce its Ascend 920, a potential substitute for the H20, in the second half of this year, _DigiTimes Asia_.

**Behind the news:** The U.S. government’s many moves to restrict shipments of advanced processors to China have sought to protect the nation’s lead in AI, but they have not prevented Chinese developers from closing the gap. In 2020, the U.S. chip makers that use U.S. technology — which includes both domestic chip designers like Nvidia and makers of advanced fabrication equipment like the Netherlands’ ASML — to seek permission before doing business with Chinese tech giant Huawei. Last December, the U.S. published sweeping limits on sales of processors that involve U.S. technology, as well as the technology itself, to Chinese businesses.
**Yes, but:** Export restrictions may have slowed China’s production of advanced chips, but they have also incentivized China to invest in in AI. In January, the Chinese AI developer DeepSeek surprised U.S. policymakers and AI leaders with the release of [DeepSeek-R1](https://www.deeplearning.ai/the-batch/deepseek-r1-an-affordable-rival-to-openais-o1/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj), which performs comparably to OpenAI’s o1, but whose weights are freely available and trained using less computation.
**Why it matters:** The first wave of restrictions on sales of advanced chips to China did to U.S. chipmakers, largely because . But later restrictions have had a greater on their sales. The new limits could cost Nvidia and AMD significant revenue and likely will their competitiveness abroad and China’s homegrown chip-making industry.
**We’re thinking:** The AI community’s international scope is one of its greatest strengths. While individual countries must attend to their national security, progress in AI benefits all nations. Even in this era of rising protectionism, we hope members of the global AI community continue to support one another and encourage the free flow of ideas.
![AI diagram showing generator and scorer loop to produce final output based on test image of a cat.](https://dl-staging-website.ghost.io/content/images/2025/04/unnamed--80-.png)

# Text-Only LLM Goes Multimodal

Large language models excel at processing text but can’t interpret images, video, or audio directly without further training on those media types. Researchers devised a way to overcome this limitation.
**What’s new:** Kumar Ashutosh and colleagues at Meta, University of Texas, and UC Berkeley introduced (MILS), a method that pairs a text-only large language model (LLM) with a multimodal embedding model to generate captions for images, video, and audio without further training.
**Key insight:** LLMs can generate text and refine their outputs based on new information. On the other hand, multimodal embedding models can score the similarity between a given text and an image, video, or audio clip. Given this score, an LLM can regenerate the text iteratively until the score indicates a strong match between the text and the associated media. This enables the LLM to generate accurate captions for images, videos, and audio clips without training in these tasks.
**How it works:** Given a prompt and an image, video, or audio clip, Llama 3.1 8B produced and iteratively refined the prompt according to a pretrained multimodal embedding model’s estimate of the similarity between the text and media.

- The LLM generated 30,000 to 50,000 initial captions to prime the process.
- Given each caption and a media file, a multimodal model estimated their semantic similarity scores. evaluated text and images, text and video, and [ImageBind](https://www.deeplearning.ai/the-batch/imagebind-the-ai-model-that-binds-data-from-six-data-types-at-once/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9uRHc917kJGLYRkEAyGhBfTODFwWNzcGx6XckCf9IJBxkUGcTubXI-IZpFHmRpRuvEdhj) text and audio.
- Based on the top 50 most-similar previous captions, the LLM generated new captions.
- The system repeated the previous two steps until the top-scoring texts changed little or the LLM reached a predetermined number of iterations.

**Results:** The authors evaluated MILS on captioning images, videos, and audio clips. They measured performance according to Metric for Evaluation of Translation with Explicit ORdering (METEOR), which checks for synonyms, words that share the same root, and word order to determine whether a generated caption matches a ground-truth caption (higher is better). Overall, MILS outperformed models that underwent task-specific training.

- On the dataset for image captioning, MILS achieved 15.0 METEOR, while achieved 14.1 METEOR.
- On , which evaluates video captioning, MILS attained 14.4 METEOR, while a trained to caption videos achieved 11.3 METEOR.
- On , which assesses audio captions, MILS achieved a METEOR of 12.4, while reached 9.4 METEOR.

**Why it matters:** Zero-shot captioning models like Aya Vision and Pixtral require training on paired captions and media. The authors’ approach takes advantage of pretrained multimodal models to enable an LLM to compose multimedia captions without further training.
**We’re thinking:** Synthetic data is increasingly useful for training AI models. By enabling LLMs to synthesize good captions, MILS adds fuel to this fire.
![](https://www.deeplearning.ai/_next/image/?url=https%3A%2F%2Fhome-wordpress.deeplearning.ai%2Fwp-content%2Fuploads%2F2024%2F10%2FDE-Vertical-2.png&w=3840&q=75)
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
