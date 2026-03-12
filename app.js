const modal = document.getElementById("lyricsModal")
const closeBtn = document.getElementById("closeLyrics")
const mount = document.getElementById("lyricsEmbedMount")
const titleEl = document.getElementById("lyricsTitle")

document.querySelectorAll(".lyricsBtn").forEach(btn=>{
btn.addEventListener("click",()=>{
const url = btn.dataset.lyrics
openLyrics(url)
})
})

closeBtn.onclick=()=>{
modal.classList.add("hidden")
mount.innerHTML=""
}

/* ---------- Extract Genius Song ID ---------- */

async function fetchSongIdFromGenius(url){

try{

const res = await fetch(url)
const html = await res.text()

/* look for embed container */

let match = html.match(/data-song-id="(\d+)"/)

if(match) return match[1]

/* fallback search */

match = html.match(/song_id\":(\d+)/)

if(match) return match[1]

return null

}catch(e){

console.error("Lyrics fetch failed",e)
return null

}

}

/* ---------- Load Genius Embed ---------- */

function loadEmbed(songId,url){

mount.innerHTML="Loading lyrics..."

const containerId=`rg_embed_link_${songId}`

mount.innerHTML=`

<div
id="${containerId}"
class="rg_embed_link"
data-song-id="${songId}">
Read <a href="${url}">Lyrics</a> on Genius
</div>

`

const script=document.createElement("script")
script.src=`https://genius.com/songs/${songId}/embed.js`
script.async=true
script.crossOrigin="anonymous"

document.body.appendChild(script)

}

/* ---------- Main Modal Logic ---------- */

async function openLyrics(url){

modal.classList.remove("hidden")
titleEl.textContent="Lyrics"

mount.innerHTML="Finding lyrics..."

const songId = await fetchSongIdFromGenius(url)

if(!songId){

mount.innerHTML=`

<div>
Lyrics embed unavailable.<br>
<a href="${url}" target="_blank">Open on Genius</a>
</div>

`

return
}

loadEmbed(songId,url)

}