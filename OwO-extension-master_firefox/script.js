

var faces = ["(・`ω´・)",
             ";;w;;",
             "owo",
             "UwU", 
             ">w<", 
             "^w^", 
             "ÕWÕ", 
             "O W O",
             "(*^ω^)", 
             "(◕‿◕✿)", 
             "(◕ᴥ◕)", 
             "ʕ•ᴥ•ʔ", 
             "ʕ￫ᴥ￩ʔ", 
             "(*^.^*)", 
             "owo", 
             "(｡♥‿♥｡)", 
             "uwu", 
             "(*￣з￣)", 
             ">w<", 
             "^w^", 
             "(つ✧ω✧)つ", 
             "(/ =ω=)/",
             "٩◔̯◔۶",
             "☼.☼",
             "(▰˘◡˘▰)",
             "ಠ~ಠ",
             "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧",
             "♪~ ᕕ(ᐛ)ᕗ",
             "ᕙ(⇀‸↼‶)ᕗ",
             "ᕦ(ò_óˇ)ᕤ",
             "(｡◕‿‿◕｡)",
             "ლ(́◉◞౪◟◉‵ლ)",
             "༼ つ ◕_◕ ༽つ",
             "(｀◔ ω ◔´)",
             "ʕ◉.◉ʔ",
             "ฅ^•ﻌ•^ฅ",
             "✧ʕ̢̣̣̣̣̩̩̩̩·͡˔·ོɁ̡̣̣̣̣̩̩̩̩✧",
             "V●ᴥ●V",
             "٩( ᐛ )و",
             "ʕ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ",
             "(ง^ᗜ^)ง",
             "ฅ^•ﻌ•^ฅ",
             "(ʘᗝʘ)",
             "(❍ᴥ❍ʋ)"
             ];

function OwoifyText(v) {
    v = v.replace(/ove/g, 'uv');
    v = v.replace(/the/g, 'de');
    v = v.replace(/The/g,'De');
    v = v.replace(/THE/g,'DE');
    v = v.replace(/(?:r|l)/g, "w");
    v = v.replace(/(?:R|L)/g, "W");
    v = v.replace(/n([aeiou])/g, 'ny$1');
    v = v.replace(/([])([aeiou])/g, '$1w$2');
    v = v.replace(/N([aeiou])/g, 'Ny$1');
    v = v.replace(/N([AEIOU])/g, 'NY$1');
    v = v.replace(/ove/g, "uv");
    v = v.replace(/ is /g,' ish ');
    v = v.replace(/ Is /g,' Ish ');
    v = v.replace(/([bcfghjkmpqstvxz])([aeiou])/g, '$1w$2');
    v = v.replace(/([BCFGHJKMPQSTVXZ])([aeiou])/g, '$1w$2');
    v = v.replace(/([BCFGHJKMPQSTVXZ])([AIEOU])/g, '$1W$2');
    v = v.replace(/th/g, 'd');
    v = v.replace(/Th/g, 'D');
    v = v.replace(/TH/g, 'D');
    v = v.replace(/[\!\.\,\?]/g, " " + faces[Math.floor(Math.random() * faces.length)] + " ");
    return v;
};

// Verwandelt die Elemente in OwO Text
var tags = ['span','label','#text',
            'div','h1','h2','h3',
            'summary','p','button',
            'input','li','tr',
            'tbody','td','table',
            'a','yt-formatted-string',
            'strong','b','pre','code',
            'yt-formatted-string[has-link-only_]:not([force-default-style]) a.yt-simple-endpoint.yt-formatted-string',
            'yt-formatted-string.ytd-video-primary-info-renderer',
            '#description', 'yt-formatted-string', 'span:nth-child(1)',
            '.css-901oao', '.bqe', '.msg707116971022295815 td', 'i', 'cite'];



just_why();
var time = 1*1000
let timeId = setInterval(just_why, time);
// chrome.webRequest.onCompleted.addListener(function() {just_why()});


function just_why() {
    for (let i =0; i < tags.length; i++) {
        die(tags[i]);
    }
}


function die(tag) {
    
    $(tag).contents().filter(function () {
        return this.nodeType == 3;
    }).each(function () {
        this.nodeValue = this.nodeValue.replace(this.nodeValue, OwoifyText(this.nodeValue));
    });
}