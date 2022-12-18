
Needs:
* Standardized system to system bus
  * similar to a transformers pipeline
* Standardized subsystem module bus
  * probably a layer over TF
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
* Short term memory
  * tensor weights
  * input 
  * selected output
  * was it executed
  * sentiment of simulation
  * sentiment of outcome (later with retraining)
* Scene Simulator
  * image diffusion
  * motion diffusion
    * https://anuragajay.github.io/decision-diffuser/
  * motion prediction
  * spatial mapping
    * https://twitter.com/LumaLabsAI
    * use image diffusion as sprites/textures
    * depth maps will be good here since all/most images are from a 1st person perspective so the generated depth map will nearly always match the perspective of the user
  * dreambooth-style individual-based fine-tuning
    * identify participants in scenario
    * when simulating their replies, use this fine-tuned model
    * further fine tune with every interaction
    * figure out way to identify similar participants to known participants and make blended models as the starting point
    * maintain participant-indexed memory
  * per-entity models/pocket sims
    * each encountered entity gets a dedicated model fine tuned on interactions with that entity
    * fine-tuned models
    * textual inversion?
    * hypernetworks?
* Judge
  * Reinforcement-based learning
  * The "cringe" circuit: continuously reasses past decisions and outcomes
  * Quorum of "trusted" pocket sims/per-entity model
  * Training set
    * internet archive
    * project guttenberglakhglahglka
      * per [The One Guy](https://github.com/TheOneTrueGuy): files in project g have boilerplate intro and legal jargon so those will need to be preprocessed out
    * google books
    * movies
    * scentific renders
    * crafted simulations
    * https://twitter.com/du_yilun/status/1597618021342023680
  * https://twitter.com/icodeblockchain/status/1599882951923466240
* Output Bus
  * https://github.com/leggedrobotics/



Misc Notes:
* proximal policy optimization for judgement (thanks @TheOneTrueGuy)
  * https://arxiv.org/abs/1707.06347 
  * https://www.youtube.com/watch?v=hlv79rcHws0 
  * https://github.com/nat/natbot
* nd-gravity distance?
* Products
  * anomoly detection
  * social media assistant/digital clones
  * chat bot
  * reality filter
  * proactive friend
    * calls
    * DMs
    * using the per-entity simulations to be the best friend/companion possible
* Logins/user accounts
  * for any API/product that requires login, make it as low-friction as possible
  * Metamask
  * Google login
* try storing prototype initial noise per token or token combo
  * when token comes up, use that seed as a starting point? might converge faster, might not work
* https://twitter.com/Guygies/status/1604528812292968449
  * "We saw benefits when residual weights were shared between the components of a GAN so it would make sense for internals to share tensors. It could then assemble its own temporary gans & exploit in-context learning to refine tasks" [The One Guy](https://github.com/TheOneTrueGuy)
  * 



  