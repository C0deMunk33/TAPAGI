
Needs:
* Text to Text
  * Google T5
  * OpenAI GPT-*
  * Nvidia Megatron-LM
  * Microsoft Turning-NLG
  * Bloom
    * https://bigscience.huggingface.co/blog/bloom
* Text to Speech
  * https://huggingface.co/models?pipeline_tag=text-to-speech&sort=downloads
  * https://www.youtube.com/watch?v=aLBedWj-5CQ
* Audio to Text
  * Whisper
* IRL Simulator
  * image diffusion
  * motion diffusion
    * https://anuragajay.github.io/decision-diffuser/
  * motion prediction
  * spatial mapping
    * https://twitter.com/LumaLabsAI
  * dreambooth-style individual-based fine-tuning
    * identify participants in scenario
    * when simulating their replies, use this fine-tuned model
    * further fine tune with every interaction
    * figure out way to identify similar participants to known participants and make blended models as the starting point
    * maintain participant-indexed memory
  * per-entity models: each encountered entity gets a dedicated model fine tuned on interactions with that entity
* Judge
  * Reinforcement-based learning
  * The "cringe" circuit: continuously reasses past decisions and outcomes
  * Training set
    * internet archive
    * project guttenberglakhglahglka
    * google books
    * movies
    * scentific renders
    * crafted simulations
    * https://twitter.com/du_yilun/status/1597618021342023680
  * https://twitter.com/icodeblockchain/status/1599882951923466240



Misc Notes:
* proximal policy optimization for judgement (thanks @TheOneTrueGuy)
  * https://arxiv.org/abs/1707.06347 
  * https://www.youtube.com/watch?v=hlv79rcHws0 
  * https://github.com/nat/natbot
* nd-gravity distance?