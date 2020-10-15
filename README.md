Youtube to MP3
by Julio Neto

What Is This?
This is a (very) simple Python app to convert Youtube videos into mp3 files locally in your machine. No more suspect websites needed to do that.

How To Use This
1) Make sure you have Python installed in your computer.
2) Run pip install -r requirements.txt to install dependencies
3) Run python yt2mp3.py
4) When prompted, copy/paste the full address from the Youtube video (like https://youtu.be/xpto)
5) Your mp3 file will be saved in the same folder/directory where yt2mp3.py is.

Why should I use it?
I used to run while listening to Spotify on my smartwatch. After a while, I get tired of it. Then, I realized most YT videos are so rich in audio content (like Neil deGrasse Tyson's videos) that they could help me to run for much more time without getting bored.
So I started using websites to convert YT to MP3. However, they are quite slow and full of advertisements. 
To solve this, I put these incredible modules (youtube-dl and audiosegment) to work together.

ps: Why am I not using Youtube-dl to convert directly to MP3 format? I tried but I got better quality and size converting first to wav, then using Audiosegment to convert it to mp3 =)
