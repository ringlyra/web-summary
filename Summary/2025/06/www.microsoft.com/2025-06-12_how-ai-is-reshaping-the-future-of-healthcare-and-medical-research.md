---
title: How AI is reshaping the future of healthcare and medical research - Microsoft
  Research
source: https://www.microsoft.com/en-us/research/podcast/how-ai-is-reshaping-the-future-of-healthcare-and-medical-research/
author:
- www.microsoft.com
published: '2025-06-12T16:17:04+00:00'
fetched: '2025-06-15T10:24:42.050207+00:00'
tags:
- codex
- ai
- healthcare
- microsoft
- podcast
image: ''
---

## 要約

Microsoft ResearchのPeter Leeが、生成AIが医療をどのように変革しているかを探るポッドキャスト。ビル・ゲイツとOpenAIのSebastien Bubeckを迎え、GPT-4誕生以降の医療分野での利用実態と新たな可能性を議論する。両者は、臨床現場でのAI活用拡大や途上国支援、評価基準の整備の重要性を強調。医療提供と研究で異なる変化が起きており、データを活用した個別化診療が現実味を帯びてきたと語る。ゲイツは安価な知能の時代の到来を指摘し、世界の医療格差をAIで補う未来を期待。ブーベックは数学的視点からLLMを検証し、HealthBenchやADeLeなど新たな評価手法の意義を紹介。番組は、AIが診断支援や医療研究を促進する強力なツールになると結んでいる。

## 本文

In November 2022, OpenAI’s ChatGPT kick-started a new era in AI. This was followed less than a half year later by the release of GPT-4. In the months leading up to GPT-4’s public release, Peter Lee, president of Microsoft Research, cowrote a book full of optimism for the potential of advanced AI models to transform the world of healthcare. What has happened since? In this special podcast series, _The AI Revolution in Medicine, Revisited_, Lee revisits the book, exploring how patients, providers, and other medical professionals are experiencing and using generative AI today while examining what he and his coauthors got right—and what they didn’t foresee.

In this episode, Microsoft co-founder and Gates Foundation Chair[Bill Gates (opens in new tab)](https://www.gatesnotes.com/meet-bill) and OpenAI research lead [Sébastien Bubeck (opens in new tab)](http://sbubeck.com/), formerly Microsoft’s VP of AI, join Lee to discuss how they’re seeing generative AI’s adoption in healthcare unfolding globally and the opportunities for further adoption, such as the development of proper benchmarks. Together, the three use insights drawn from unparalleled access to the continuing evolution of AI to explore the yet untapped potential of the technology to empower clinicians and patients alike and talk about the urgency to create AI-driven healthcare systems in underserved countries. They also reflect on the distinction between healthcare _delivery_ and healthcare _discovery_ and how the type and pace of change brought on by AI may differ for each.

Transcript
----------

[MUSIC]

[BOOK PASSAGE]

**PETER LEE:**“In ‘The Little Black Bag,’ a classic science fiction story, a high-tech doctor’s kit of the future is accidentally transported back to the 1950s, into the shaky hands of a washed-up, alcoholic doctor. The ultimate medical tool, it redeems the doctor wielding it, allowing him to practice gratifyingly heroic medicine. … The tale ends badly for the doctor and his treacherous assistant, but it offered a picture of how advanced technology could transform medicine—powerful when it was written nearly 75 years ago and still so today.What would be the Al equivalent of that little black bag? At this moment when new capabilities are emerging, how do we imagine them into medicine?”

[END OF BOOK PASSAGE]

[THEME MUSIC]

This is _The AI Revolution in Medicine, Revisited_. I’m your host, Peter Lee.

Shortly after OpenAI’s GPT-4 was publicly released, Carey Goldberg, Dr. Zak Kohane, and I published _The AI Revolution in Medicine_ to help educate the world of healthcare and medical research about the transformative impact this new generative AI technology could have. But because we wrote the book when GPT-4 was still a secret, we had to speculate. Now, two years later, what did we get right, and what did we get wrong?

In this series, we’ll talk to clinicians, patients, hospital administrators, and others to understand the reality of AI in the field and where we go from here.

[THEME MUSIC FADES]

The book passage I read at the top is from “Chapter 10: The Big Black Bag.”

In imagining AI in medicine, Carey, Zak, and I included in our book two fictional accounts. In the first, a medical resident consults GPT-4 on her personal phone as the patient in front of her crashes. Within seconds, it offers an alternate response based on recent literature. In the second account, a 90-year-old woman with several chronic conditions is living independently and receiving near-constant medical support from an AI aide.

In our conversations with the guests we’ve spoken to so far, we’ve caught a glimpse of these predicted futures, seeing how clinicians and patients are _actually_ using AI today and how developers are leveraging the technology in the healthcare products and services they’re creating. In fact, that first fictional account isn’t so fictional after all, as most of the doctors in the real world actually appear to be using AI at least occasionally—and sometimes much more than occasionally—to help in their daily clinical work. And as for the second fictional account, which is more of a _science fiction_ account, it seems we are indeed on the verge of a new way of delivering and receiving healthcare, though the future is still very much open.

As we continue to examine the current state of AI in healthcare and its potential to transform the field, I’m pleased to welcome Bill Gates and Sébastien Bubeck.

Bill may be best known as the co-founder of Microsoft, having created the company with his childhood friend Paul Allen in 1975. He’s now the founder of Breakthrough Energy, which aims to advance clean energy innovation, and TerraPower, a company developing groundbreaking nuclear energy and science technologies. He also chairs the world’s largest philanthropic organization, the Gates Foundation, and focuses on solving a variety of health challenges around the globe and here at home.

Sébastien is a research lead at OpenAI. He was previously a distinguished scientist, vice president of AI, and a colleague of mine here at Microsoft, where his work included spearheading the development of the family of small language models known as Phi. While at Microsoft, he also coauthored the discussion-provoking 2023 paper “[Sparks of Artificial General Intelligence](https://www.microsoft.com/en-us/research/publication/sparks-of-artificial-general-intelligence-early-experiments-with-gpt-4/?msockid=35739e94ab6c69d41b738b93aa076831),” which presented the results of early experiments with GPT-4 conducted by a small team from Microsoft Research.

[TRANSITION MUSIC]

Here’s my conversation with Bill Gates and Sébastien Bubeck.

**LEE:** Bill, welcome.

**BILL GATES:** Thank you.

**LEE:** Seb …

**SÉBASTIEN BUBECK:** Yeah. Hi, hi, Peter. Nice to be here.

**LEE:** You know, one of the things that I’ve been doing just to get the conversation warmed up is to talk about origin stories, and what I mean about origin stories is, you know, what was the first contact that you had with large language models or the concept of generative AI that convinced you or made you think that something really important was happening?

And so, Bill, I think I’ve heard the story about, you know, the time when the OpenAI folks—Sam Altman, Greg Brockman, and others—showed you something, but could we hear from you what those early encounters were like and what was going through your mind?

**GATES:** Well, I’d been visiting OpenAI soon after it was created to see things like GPT-2 and to see the little arm they had that was trying to match human manipulation and, you know, looking at their games like Dota that they were trying to get as good as human play. And honestly, I didn’t think the language model stuff they were doing, even when they got to GPT-3, would show the ability to learn, you know, in the same sense that a human reads a biology book and is able to take that knowledge and access it not only to pass a test but also to create new medicines.

And so my challenge to them was that if their LLM could get a five on the advanced placement biology test, then I would say, OK, it took biologic knowledge and encoded it in an accessible way and that I didn’t expect them to do that very quickly but it would be profound.

And it was only about six months after I challenged them to do that, that an early version of GPT-4 they brought up to a dinner at my house, and in fact, it answered most of the questions that night very well. The one it got totally wrong, we were … because it was so good, we kept thinking, _Oh, we must be wrong_. It turned out it was a math weakness [LAUGHTER] that, you know, we later understood that that was an area of, weirdly, of incredible weakness of those early models. But, you know, that was when I realized, OK, the age of cheap intelligence was at its beginning.

**LEE:** Yeah. So I guess it seems like you had something similar to me in that my first encounters, I actually harbored some skepticism. Is it fair to say you were skeptical before that?

**GATES:** Well, the idea that we’ve figured out how to encode and access knowledge in this very deep sense without even understanding the nature of the encoding, …

**LEE:** Right.

**GATES:** … that is a bit weird.

**LEE:** Yeah.

**GATES:** We have an algorithm that creates the computation, but even say, OK, where is the president’s birthday stored in there? Where is this fact stored in there? The fact that even _now_ when we’re playing around, getting a little bit more sense of it, it’s opaque to us what the semantic encoding is, it’s, kind of, amazing to me. I thought the invention of knowledge storage would be an explicit way of encoding knowledge, not an implicit statistical training.

**LEE:** Yeah, yeah. All right. So, Seb, you know, on this same topic, you know, I got—as we say at Microsoft—I got pulled into the tent. [LAUGHS]

**BUBECK:** Yes.

**LEE:** Because this was a very secret project. And then, um, I had the opportunity to select a small number of researchers in MSR [Microsoft Research] to join and start investigating this thing seriously. And the first person I pulled in was _you_.

**BUBECK:** Yeah.

**LEE:** And so what were your first encounters? Because I actually don’t remember what happened then.

**BUBECK:** Oh, I remember it very well. [LAUGHS] My first encounter with GPT-4 was in a meeting with the two of you, actually. But my kind of first contact, the first moment where I realized that something was happening with generative AI, was before that. And I agree with Bill that I also wasn’t too impressed by GPT-3.

I though that it was kind of, you know, very naturally mimicking the web, sort of parroting what was written there in a nice way. Still in a way which seemed very impressive. But it wasn’t really intelligent in any way. But shortly after GPT-3, there was a model before GPT-4 that really shocked me, and this was the first image generation model, DALL-E 1.

So that was in 2021. And I will forever remember the press release of OpenAI where they had this prompt of an avocado chair and then you had this image of the avocado chair. [LAUGHTER] And what really shocked me is that clearly the model kind of “understood” what is a chair, what is an avocado, and was able to merge those concepts.

So this was really, to me, the first moment where I saw some understanding in those models.

**LEE:**So this was, just to get the timing right, that was before I pulled you into the tent.

**BUBECK:**That was before. That was like a year before.

**LEE:**Right.

**BUBECK:**And now I will tell you how, you know, we went from that moment to the meeting with the two of you and GPT-4.

So once I saw this kind of understanding, I thought, OK, fine. It understands concept, but it’s still not able to reason. It cannot—as, you know, Bill was saying—it cannot learn from your document. It cannot reason.

So I set out to try to _prove_ that. You know, this is what I was in the business of at the time, trying to prove things in mathematics. So I was trying to prove that basically autoregressive transformers could _never_ reason. So I was trying to prove this. And after a year of work, I had something reasonable to show. And so I had the meeting with the two of you, and I had this example where I wanted to say, there is no way that an LLM is going to be able to do _x_.

And then as soon as I … I don’t know if you remember, Bill. But as soon as I said that, you said, oh, but wait a second. I had, you know, the OpenAI crew at my house recently, and they showed me a new model. Why don’t we ask this new model this question?

**LEE:**Yeah.

**BUBECK:**And we did, and it solved it on the spot. And that really, honestly, just changed my life. Like, you know, I had been working for a year trying to say that this was impossible. And just right there, it was shown to be possible.

**LEE:** [LAUGHS] One of the very first things I got interested in—because I was really thinking a lot about healthcare—_was_ healthcare and medicine.

And I don’t know if the two of you remember, but I ended up doing a lot of tests. I ran through, you know, step one and step two of the US Medical Licensing Exam. Did a whole bunch of other things. I wrote this big report. It was, you know, I can’t remember … a couple hundred pages.

And I needed to share this with someone. I didn’t … there weren’t too many people I could share it with. So I sent, I think, a copy to you, Bill. Sent a copy to you, Seb.

I hardly slept for about a week putting that report together. And, yeah, and I kept working on it. But I was far from alone. I think everyone who was in the tent, so to speak, in those early days was going through something pretty similar. All right. So I think … of course, a lot of what I put in the report also ended up being examples that made it into the book.

But the main purpose of this conversation isn’t to reminisce about [LAUGHS] or indulge in those reminiscences but to talk about what’s happening in healthcare and medicine. And, you know, as I said, we wrote this book. We did it very, very quickly. Seb, you helped. Bill, you know, you provided a review and some endorsements.

But, you know, honestly, we didn’t know what we were talking about because no one had access to this thing. And so we just made a bunch of guesses. So really, the whole thing I wanted to probe with the two of you is, now with two years of experience out in the world, what, you know, what do we think is happening today?

You know, is AI actually having an impact, positive or negative, on healthcare and medicine? And what do we now think is going to happen in the next two years, five years, or 10 years? And so I realize it’s a little bit too abstract to just ask it that way. So let me just try to narrow the discussion and guide us a little bit.

Um, the kind of administrative and clerical work, paperwork, around healthcare—and we made a lot of guesses about that—that appears to be going well, but, you know, Bill, I know we’ve discussed that sometimes that you think there ought to be a lot more going on.Do you have a viewpoint on how AI is actually finding its way into reducing paperwork?

**GATES:** Well, I’m stunned … I don’t think there should be a patient-doctor meeting where the AI is not sitting in and both transcribing, offering to help with the paperwork, and even making suggestions, although the doctor will be the one, you know, who makes the final decision about the diagnosis and whatever prescription gets done.

It’s so helpful. You know, when that patient goes home and their, you know, son who wants to understand what happened has some questions, that AI should be available to continue that conversation. And the way you can improve that experience and streamline things and, you know, involve the people who advise you. I don’t understand why that’s not more adopted, because there you still have the human in the loop making that final decision.

But even for, like, follow-up calls to make sure the patient did things, to understand if they have concerns and knowing when to escalate back to the doctor, the benefit is incredible. And, you know, that thing is ready for prime time. That paradigm is ready for prime time, in my view.

**LEE:** Yeah, there are some good products, but it seems like the number one use right now—and we kind of got this from some of the previous guests in previous episodes—is the use of AI just to respond to emails from patients. [LAUGHTER] Does that make sense to you?

**BUBECK:** Yeah. So maybe I want to second what Bill was saying but maybe take a step back first. You know, two years ago, like, the concept of clinical scribes, which is one of the things that we’re talking about right now, it would have sounded, in fact, it sounded two years ago, borderline dangerous. Because everybody was worried about hallucinations. What happened if you have this AI listening in and then it transcribes, you know, something wrong?

Now, two years later, I think it’s mostly working. And in fact, it is not yet, you know, fully adopted. You’re right. But it is in production. It is used, you know, in many, many places. So this rate of progress _is_ astounding because it wasn’t obvious that we would be able to overcome those obstacles of hallucination. It’s not to say that hallucinations are fully solved. In the case of the closed system, they are.

Now, I think more generally what’s going on in the background is that there is something that we, that certainly I, underestimated, which is this management overhead. So I think the reason why this is not adopted everywhere is really a training and teaching aspect. People need to be taught, like, those systems, how to interact with them.

And one example that I really like, a study that recently appeared where they tried to use ChatGPT for diagnosis and they were [comparing doctors without and with ChatGPT (opens in new tab)](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395). And the amazing thing … so this was a set of cases where the accuracy of the doctors alone was around 75%. ChatGPT alone was 90%. So that’s already kind of mind blowing. But then the kicker is that doctors with ChatGPT was 80%.

Intelligence alone is not enough. It’s also how it’s presented, how you interact with it. And ChatGPT, it’s an amazing tool. Obviously, I absolutely love it. But it’s not … you don’t want a doctor to have to type in, you know, prompts and use it that way.

It should be, as Bill was saying, kind of running continuously in the background, sending you notifications. And you have to be really careful of the rate at which those notifications are being sent. Because if they are too frequent, then the doctor will learn to ignore them. So you have to … all of those things matter, in fact, at least as much as the level of intelligence of the machine.

**LEE:** One of the things I think about, Bill, in that scenario that you described, doctors do some thinking about the patient when they write the note. So, you know, I’m always a little uncertain whether it’s actually … you know, you wouldn’t necessarily want to fully automate this, I don’t think. Or at least there needs to be some prompt to the doctor to make sure that the doctor puts some thought into what happened in the encounter with the patient. Does that make sense to you at all?

**GATES:** At this stage, you know, I’d still put the onus on the doctor to write the conclusions and the summary and not delegate that.

The tradeoffs you make a little bit are somewhat dependent on the situation you’re in. If you’re in Africa,where most people never meet a real doctor their entire life, the idea of being able to have some of this advice and diagnosis is extremely advantageous because you’re comparing it to nothing.

So, yes, the doctor’s still going to have to do a lot of work, but just the quality of letting the patient and the people around them interact and ask questions and have things explained, that alone is such a quality improvement. It’s mind blowing.

**LEE:** So since you mentioned, you know, Africa—and, of course, this touches on the mission and some of the priorities of the Gates Foundation and this idea of democratization of access to expert medical care—what’s the most interesting stuff going on right now? Are there people and organizations or technologies that are impressing you or that you’re tracking?

**GATES:** Yeah. So the Gates Foundation has given out a lot of grants to people in Africa doing education, agriculture but more healthcare examples than anything. And the way these things start off, they often start out either being patient-centric in a narrow situation, like, _OK, I’m a pregnant woman; talk to me_. Or, _I have infectious disease symptoms; talk to me_. Or they’re connected to a health worker where they’re helping that worker get their job done. And we have lots of pilots out, you know, in both of those cases.

The dream would be eventually to have the thing the patient consults be so broad that it’s like having a doctor available who understands the local things.

**LEE:**Right.

**GATES:**We’re not there yet. But over the next two or three years, you know, particularly given the worsening financial constraints against African health systems, where the withdrawal of money has been dramatic, you know, figuring out how to take this—what I sometimes call “free intelligence”—and build a quality health system around that, we will have to be more radical in low-income countries than any rich country is ever going to be.

**LEE:** Also, there’s maybe a different regulatory environment, so some of those things maybe are easier? Because right now, I think the world hasn’t figured out how to and whether to regulate, let’s say, an AI that might give a medical diagnosis or write a prescription for a medication.

**BUBECK:** Yeah. I think one issue with this, and it’s also slowing down the deployment of AI in healthcare more generally, is a lack of proper benchmark. Because, you know, you were mentioning the USMLE [United States Medical Licensing Examination], for example. That’s a great test to test _human beings_ and _their_ knowledge of healthcare and medicine. But it’s not a great test to give to an AI.

It’s not asking the right questions. So finding what are the right questions to test whether an AI system is ready to give diagnosis in a constrained setting, that’s a very, very important direction, which to my surprise, is not yet accelerating at the rate that I was hoping for.

**LEE:** OK, so that gives me an excuse to get more now into the core AI tech because something I’ve discussed with both of you is this issue of what are the right tests. And you both know the very first test I give to any new spin of an LLM is I present a patient, the results—a _mythical_ patient—the results of my physical exam, my _mythical_ physical exam. Maybe some results of some initial labs. And then I present or propose a differential diagnosis. And if you’re not in medicine, a differential diagnosis you can just think of as a prioritized list of the possible diagnoses that fit with all that data. And in that proposed differential, I always intentionally make two mistakes.

I make a textbook technical error in one of the possible elements of the differential diagnosis, and I have an error of omission. And, you know, I just want to know, does the LLM understand what I’m talking about? And all the good ones out there do now. But then I want to know, can it spot the errors? And then most importantly, is it willing to tell me I’m wrong, that I’ve made a mistake?

That last piece seems really hard for AI today. And so let me ask you first, Seb, because at the time of this taping, of course, there was a new spin of GPT-4o last week that became _overly_ sycophantic. In other words, it was actually prone in that test of mine not only to _not_ tell me I’m wrong, but it actually praised me for the creativity of my differential. [LAUGHTER] What’s up with that?

**BUBECK:** Yeah, I guess it’s a testament to the fact that training those models is still more of an art than a science. So it’s a difficult job. Just to be clear with the audience, we have rolled back that [LAUGHS] version of GPT-4o, so now we don’t have the sycophant version out there.

Yeah, no, it’s a really difficult question. It has to do … as you said, it’s very technical. It has to do with the post-training and how, like, where do you nudge the model? So, you know, there is this very classical by now technique called RLHF [reinforcement learning from human feedback], where you push the model in the direction of a certain reward model. So the reward model is just telling the model, you know, what behavior is good, what behavior is bad.

But this reward model is itself an LLM, and, you know, Bill was saying at the very beginning of the conversation that we don’t really understand how those LLMs deal with concepts like, you know, where is the capital of France located? Things like that. It is the same thing for this reward model. We don’t know why it says that it prefers one output to another, and whether this is correlated with some sycophancy is, you know, something that we discovered basically just now. That if you push too hard in optimization on this reward model, you will get a sycophant model.

So it’s kind of … what I’m trying to say is we became too good at what we were doing, and we ended up, in fact, in a trap of the reward model.

**LEE:** I mean, you do want … it’s a difficult balance because you do want models to follow your desires and …

**BUBECK:** It’s a very difficult, very difficult balance.

**LEE:** So this brings up then the following question for me, which is the extent to which we think we’ll need to have specially trained models for things. So let me start with you, Bill. Do you have a point of view on whether we will need to, you know, quote-unquote take AI models to med school? Have them specially trained? Like, if you were going to deploy something to give medical care in underserved parts of the world, do we need to do something special to create those models?

**GATES:** We certainly need to teach them the African languages and the unique dialects so that the multimedia interactions are very high quality. We certainly need to teach them the disease prevalence and unique disease patterns like, you know, neglected tropical diseases and malaria. So we need to gather a set of facts that somebody trying to go for a US customer base, you know, wouldn’t necessarily have that in there.

Those two things are actually very straightforward because the additional training time is small. I’d say for the next few years, we’ll also need to do reinforcement learning about the context of being a doctor and how important certain behaviors are. Humans learn over the course of their life to some degree that, I’m in a different context and the way I behave in terms of being willing to criticize or be nice, you know, how important is it? Who’s here? What’s my relationship to them?

Right now, these machines don’t have that broad social experience. And so if you know it’s going to be used for health things, a lot of reinforcement learning of the very best humans in that context would still be valuable. Eventually, the models will, having read all the literature of the world about good doctors, bad doctors, it’ll understand as soon as you say, “I want you to be a doctor diagnosing somebody.” All of the implicit reinforcement that fits that situation, you know, will be there.

**LEE:** Yeah.

**GATES:** And so I hope three years from now, we don’t have to do that reinforcement learning. But today, for any medical context, you would want a lot of data to reinforce tone, willingness to say things when, you know, there might be something significant at stake.

**LEE:** Yeah. So, you know, something Bill said, kind of, reminds me of another thing that I think we missed, which is, the context also … and the specialization also pertains to different, I guess, what we still call “modes,” although I don’t know if the idea of multimodal is the same as it was two years ago. But, you know, what do you make of all of the hubbub around—in fact, within Microsoft Research, this is a big deal, but I think we’re far from alone—you know, medical images and vision, video, proteins and molecules, cell, you know, cellular data and so on.

**BUBECK:** Yeah. OK. So there is a lot to say to everything … to the last, you know, couple of minutes. Maybe on the specialization aspect, you know, I think there is, hiding behind this, a really fundamental scientific question of whether eventually we have a singular AGI [artificial general intelligence] that kind of knows everything and you can just put, you know, explain your own context and it will just get it and understand everything.

That’s one vision. I have to say, I don’t particularly believe in this vision. In fact, we humans are not like that at all. I think, hopefully, we are general intelligences, yet we have to specialize a lot. And, you know, I did myself a lot of RL, reinforcement learning, on mathematics. Like, that’s what I did, you know, spent a lot of time doing that. And I didn’t improve on other aspects. You know, in fact, I probably degraded in other aspects. [LAUGHTER] So it’s … I think it’s an important example to have in mind.

**LEE:** I think I might disagree with you on that, though, because, like, doesn’t a model have to see both good science and bad science in order to be able to gain the ability to discern between the two?

**BUBECK:** Yeah, no, that absolutely. I think there is value in seeing the generality, in having a very broad base. But then you, kind of, specialize on verticals. And this is where also, you know, open-weights model, which we haven’t talked about yet, are really important because they allow you to provide this broad base to everyone. And then you can specialize on top of it.

**LEE:** So we have about three hours of stuff to talk about, but our time is actually running low.

**BUBECK:**Yes, yes, yes.

**LEE:** So I think I want … there’s a more provocative question. It’s almost a silly question, but I need to ask it of the two of you, which is, is there a future, you know, where AI replaces doctors or replaces, you know, medical specialties that we have today? So what does the world look like, say, five years from now?

**GATES:** Well, it’s important to distinguish healthcare discovery activity from healthcare delivery activity. We focused mostly on delivery. I think it’s very much within the realm of possibility that the AI is not only accelerating healthcare discovery but substituting for a lot of the roles of, you know, _I’m an organic chemist_, or _I run various types of assays_. I can see those, which are, you know, testable-output-type jobs but with still very high value, I can see, you know, some replacement in those areas before the doctor.

The doctor, still understanding the human condition and long-term dialogues, you know, they’ve had a lifetime of reinforcement of that, particularly when you get into areas like mental health. So I wouldn’t say in five years, either people will choose to adopt it, but it will be profound that there’ll be this nearly free intelligence that can do follow-up, that can help you, you know, make sure you went through different possibilities.

And so I’d say, yes, we’ll have doctors, but I’d say healthcare will be massively transformed in its quality and in efficiency by AI in that time period.

**LEE:** Is there a comparison, useful comparison, say, between doctors and, say, programmers, computer programmers, or doctors and, I don’t know, lawyers?

**GATES:** Programming is another one that has, kind of, a mathematical correctness to it, you know, and so the objective function that you’re trying to reinforce to, as soon as you can understand the state machines, you can have something that’s “checkable”; that’s correct. So I think programming, you know, which is weird to say, that the machine will beat us at most programming tasks before we let it take over roles that have deep empathy, you know, physical presence and social understanding in them.

**LEE:** Yeah. By the way, you know, I fully expect in five years that AI will produce mathematical proofs that are checkable for validity, _easily checkable_, because they’ll be written in a proof-checking language like Lean or something but will be so complex that no human mathematician can understand them. I expect that to happen.

I can imagine in some fields, like cellular biology, we could have the same situation in the future because the molecular pathways, the chemistry, biochemistry of human cells or living cells is as complex as any mathematics, and so it seems possible that we may be in a state where in wet lab, we see, _Oh yeah, this actually works_, but no one can understand why.

**BUBECK:** Yeah, absolutely. I mean, I think I really agree with Bill’s distinction of the discovery and the delivery, and indeed, the discovery’s when you can check things, and at the end, there is an artifact that you can verify. You know, you can run the protocol in the wet lab and see [if you have] produced what you wanted. So I absolutely agree with that.

And in fact, you know, we don’t have to talk five years from now. I don’t know if you know, but just recently, there was a [paper that was published on a scientific discovery using o3- mini (opens in new tab)](https://arxiv.org/abs/2503.23758). So this is really amazing. And, you know, just very quickly, just so people know, it was about this statistical physics model, the frustrated Potts model, which has to do with coloring, and basically, the case of three colors, like, more than two colors was open for a long time, and o3 was able to reduce the case of three colors to two colors.

**LEE:** Yeah.

**BUBECK:** Which is just, like, astounding. And this is not … this is _now_. This is happening right now. So this is something that I personally didn’t expect it would happen so quickly, and it’s due to those reasoning models.

Now, on the delivery side, I would add something more to it for the reason why doctors and, in fact, lawyers and coders will remain for a long time, and it’s because we still don’t understand how those models generalize. Like, at the end of the day, we are not able to tell you when they are confronted with a really new, novel situation, whether they will work or not.

_Nobody_ is able to give you that guarantee. And I think until we understand this generalization better, we’re not going to be willing to just let the system in the wild without human supervision.

**LEE:** But don’t human doctors, human specialists … so, for example, a cardiologist sees a patient in a certain way that a nephrologist …

**BUBECK:** Yeah.

**LEE:** … or an endocrinologist might not.

**BUBECK:** That’s right. But _another_ cardiologist will understand and, kind of, expect a certain level of generalization from their peer. And this, we just don’t have it with AI models. Now, of course, you’re exactly right. That generalization is also hard for humans. Like, if you have a human trained for one task and you put them into another task, then you don’t … you often don’t know.But you have other examples. So if you have two humans that were trained on a task and you put them on another one, then you kind of expect that they will do the same on the other task.

**LEE:** OK. You know, the podcast is focused on what’s happened over the last two years. But now, I’d like one provocative prediction about what you think the world of AI and medicine is going to be at some point in the future. You pick your timeframe. I don’t care if it’s two years or 20 years from now, but, you know, what do you think will be different about AI in medicine in _that_ future than today?

**BUBECK:** Yeah, I think the deployment is going to accelerate soon. Like, we’re really not missing very much. There is this enormous capability overhang. Like, even if progress completely stopped, with current systems, we can do a lot more than what we’re doing right now. So I think this will … this _has to be_ realized, you know, sooner rather than later.

And I think it’s probably dependent on these benchmarks and proper evaluation and tying this with regulation. So these are things that take time in human society and for good reason. But now we already are at two years; you know, give it another two years and it should be really …

**LEE:** Will AI prescribe your medicines? Write your prescriptions?

**BUBECK:** I think yes. I think yes.

**LEE:** OK. Bill?

**GATES:** Well, I think the next two years, we’ll have massive pilots, and so the amount of use of the AI, still in a copilot-type mode, you know, we should get millions of patient visits, you know, both in general medicine and in the mental health side, as well. And I think that’s going to build up both the data _and_ the confidence to give the AI some additional autonomy. You know, are you going to let it talk to you at night when you’re panicked about your mental health with some ability to escalate?

And, you know, I’ve gone so far as to tell politicians with national health systems that if they deploy AI appropriately, that the quality of care, the overload of the doctors, the improvement in the economics will be enough that their voters will be _stunned_ because they just don’t expect this, and, you know, they could be reelected [LAUGHTER] just on this one thing of fixing what is a very overloaded and economically challenged health system in these rich countries.

You know, my personal role is going to be to make sure that in the poorer countries, there isn’t some lag; in fact, in many cases, that we’ll be more aggressive because, you know, we’re comparing to having no access to doctors at all. And, you know, so I think whether it’s India or Africa, there’ll be lessons that are globally valuable because we need medical intelligence. And, you know, thank god AI is going to provide a lot of that.

**LEE:** Well, on that optimistic note, I think that’s a good way to end. Bill, Seb, really appreciate all of this.

I think the most fundamental prediction we made in the book is that AI would actually find its way into the practice of medicine, and I think that that at least has come true, maybe in different ways than we expected, but it’s come true, and I think it’ll only accelerate from here. So thanks again, both of you.

[TRANSITION MUSIC]

**GATES:** Yeah. Thanks, you guys.

**BUBECK:** Thank you, Peter. Thanks, Bill.

**LEE:**I just always feel such a sense of privilege to have a chance to interact and actually work with people like Bill and Sébastien.

With Bill, I’m always amazed at how practically minded he is. He’s really thinking about the nuts and bolts of what AI might be able to do for people, and his thoughts about underserved parts of the world, the idea that we might actually be able to empower people with access to expert medical knowledge, I think is both inspiring and amazing.

And then, Seb, Sébastien Bubeck, he’s just absolutely a brilliant mind. He has a really firm grip on the deep mathematics of artificial intelligence and brings that to bear in his research and development work. And where that mathematics takes him isn’t just into the nuts and bolts of algorithms but into philosophical questions about the nature of intelligence.

One of the things that Sébastien brought up was the state of evaluation of AI systems. And indeed, he was fairly critical in our conversation. But of course, the world of AI research and development is just moving so fast, and indeed, since we recorded our conversation, OpenAI, in fact, released a new evaluation metric that is directly relevant to medical applications, and that is something called [HealthBench](https://openai.com/index/healthbench/). And Microsoft Research also released a new evaluation approach or process called [ADeLe](https://www.microsoft.com/en-us/research/publication/general-scales-unlock-ai-evaluation-with-explanatory-and-predictive-power/).

HealthBench and ADeLe are examples of new approaches to evaluating AI models that are less about testing their knowledge and ability to pass multiple-choice exams and instead are evaluation approaches designed to assess how well AI models are able to complete tasks that actually arise every day in typical healthcare or biomedical research settings. These are examples of really important good work that speak to how well AI models work in the real world of healthcare and biomedical research and how well they can collaborate with human beings in those settings.

You know, I asked Bill and Seb to make some predictions about the future. You know, my own answer, I expect that we’re going to be able to use AI to change how we diagnose patients, change how we decide treatment options.

If you’re a doctor or a nurse and you encounter a patient, you’ll ask questions, do a physical exam, you know, call out for labs just like you do today, but then you’ll be able to engage with AI based on all of that data and just ask, you know, based on all the other people who have gone through the same experience, who have similar data, how were they diagnosed? How were they treated? What were their outcomes? And what does that mean for the patient I have right now? Some people call it the “patients like me” paradigm. And I think that’s going to become real because of AI within our lifetimes. That idea of really grounding the delivery in healthcare and medical practice through data and intelligence, I actually now don’t see any barriers to that future becoming real.

[THEME MUSIC]

I’d like to extend another big thank you to Bill and Sébastien for their time. And to our listeners, as always, it’s a pleasure to have you along for the ride. I hope you’ll join us for our remaining conversations, as well as a second coauthor roundtable with Carey and Zak.

Until next time.

[MUSIC FADES]
