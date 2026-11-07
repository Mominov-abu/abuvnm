// --- 1. PAROL ANALIZATORI (ADVANCED SECURITY CHECKER) ---
const passwordInput = document.getElementById('passwordInput');
const toggleVisibilityBtn = document.getElementById('toggleVisibility');
const meterBar = document.getElementById('meterBar');
const strengthText = document.getElementById('strengthText');
const crackTimeValue = document.getElementById('crackTimeValue');
const metricEntropy = document.getElementById('metricEntropy');
const metricLength = document.getElementById('metricLength');
const checkList = document.getElementById('checkList');

// Keng tarqalgan zaif so'zlar, ismlar va oddiy qoliplar bazasi
const commonPatterns = [
    'admin', 'password', '12345', '123456', 'qwerty', 'mominov', 'abu', 
    'uzbek', 'login', 'user', 'test', 'pass', 'welcome', 'love', '123', 
    'abc', 'root', 'support', 'secret', 'sun', 'moon', 'star'
];

passwordInput.addEventListener('input', () => {
    analyzePassword(passwordInput.value);
});

toggleVisibilityBtn.addEventListener('click', () => {
    const isPassword = passwordInput.type === 'password';
    passwordInput.type = isPassword ? 'text' : 'password';
    toggleVisibilityBtn.innerHTML = isPassword ? '<i class="fa-regular fa-eye-slash"></i>' : '<i class="fa-regular fa-eye"></i>';
});

function analyzePassword(pwd) {
    const length = pwd.length;
    metricLength.textContent = `${length} belgi`;

    if (length === 0) {
        resetAnalyzer();
        return;
    }

    const checks = {
        length: length >= 12,
        uppercase: /[A-Z]/.test(pwd),
        lowercase: /[a-z]/.test(pwd),
        numbers: /[0-9]/.test(pwd),
        symbols: /[^A-Za-z0-9]/.test(pwd)
    };

    updateChecklist(checks);

    // Lug'atdagi so'zlar yoki oddiy qoliplar qatnashganini tekshirish
    const lowerPwd = pwd.toLowerCase();
    const hasCommonPattern = commonPatterns.some(pattern => lowerPwd.includes(pattern));

    // Entropiya hisoblash
    let poolSize = 0;
    if (checks.lowercase) poolSize += 26;
    if (checks.uppercase) poolSize += 26;
    if (checks.numbers) poolSize += 10;
    if (checks.symbols) poolSize += 32;

    const entropy = Math.floor(length * (Math.log2(poolSize || 1)));
    metricEntropy.textContent = `${entropy} bit`;

    // Buzilish vaqtini hisoblash mantiqi
    let secondsToCrack;
    if (hasCommonPattern || length < 8) {
        // Agar ism, oddiy so'z yoki qisqa parol bo'lsa - lug'at hujumi orqali bir necha soniyada topiladi
        secondsToCrack = 0.5;
    } else {
        const combinations = Math.pow(poolSize || 1, length);
        const hashesPerSecond = 10000000000; // 10 Billion hashes/sec (GPU cluster)
        secondsToCrack = combinations / hashesPerSecond;
    }

    updateCrackTime(secondsToCrack, hasCommonPattern);

    // Xavfsizlik balini hisoblash (0 - 100%)
    let score = Math.min(100, Math.floor((entropy / 75) * 100));
    if (hasCommonPattern) score = Math.min(score, 25); // Agar lug'atda bo'lsa balni keskin tushiramiz

    meterBar.style.width = `${score}%`;

    if (score < 35) {
        meterBar.style.backgroundColor = 'var(--red)';
        strengthText.textContent = hasCommonPattern ? 'Zaif (Lug\'atda mavjud)' : 'Juda Zaif';
        strengthText.style.color = 'var(--red)';
    } else if (score < 65) {
        meterBar.style.backgroundColor = 'var(--yellow)';
        strengthText.textContent = 'O\'rtacha';
        strengthText.style.color = 'var(--yellow)';
    } else if (score < 85) {
        meterBar.style.backgroundColor = 'var(--cyan)';
        strengthText.textContent = 'Xavfsiz';
        strengthText.style.color = 'var(--cyan)';
    } else {
        meterBar.style.backgroundColor = 'var(--green)';
        strengthText.textContent = 'Yuqori Himoyalangan';
        strengthText.style.color = 'var(--green)';
    }
}

function updateChecklist(checks) {
    Object.keys(checks).forEach(key => {
        const li = checkList.querySelector(`[data-check="${key}"]`);
        if (li) {
            if (checks[key]) {
                li.className = 'valid';
                li.innerHTML = `<i class="fa-solid fa-check"></i> ${li.textContent.trim()}`;
            } else {
                li.className = '';
                li.innerHTML = `<i class="fa-solid fa-xmark"></i> ${li.textContent.trim()}`;
            }
        }
    });
}

function updateCrackTime(seconds, hasCommonPattern) {
    if (hasCommonPattern || seconds < 1) {
        crackTimeValue.textContent = "Bir necha soniya (Lug'at xuruji)";
        crackTimeValue.style.color = "var(--red)";
    } else if (seconds < 60) {
        crackTimeValue.textContent = `${Math.floor(seconds)} soniya`;
        crackTimeValue.style.color = "var(--red)";
    } else if (seconds < 3600) {
        crackTimeValue.textContent = `${Math.floor(seconds / 60)} daqiqa`;
        crackTimeValue.style.color = "var(--yellow)";
    } else if (seconds < 86400) {
        crackTimeValue.textContent = `${Math.floor(seconds / 3600)} soat`;
        crackTimeValue.style.color = "var(--yellow)";
    } else if (seconds < 31536000) {
        crackTimeValue.textContent = `${Math.floor(seconds / 86400)} kun`;
        crackTimeValue.style.color = "var(--cyan)";
    } else if (seconds < 31536000000) {
        crackTimeValue.textContent = `${Math.floor(seconds / 31536000)} yil`;
        crackTimeValue.style.color = "var(--green)";
    } else {
        crackTimeValue.textContent = "Ming yillab (Superkompyuter kerak)";
        crackTimeValue.style.color = "var(--green)";
    }
}

function resetAnalyzer() {
    meterBar.style.width = '0%';
    strengthText.textContent = 'Kiritilmadi';
    strengthText.style.color = 'var(--text-main)';
    crackTimeValue.textContent = '0 soniya';
    crackTimeValue.style.color = 'var(--green)';
    metricEntropy.textContent = '0 bit';
    metricLength.textContent = '0 belgi';
    checkList.querySelectorAll('li').forEach(li => {
        li.className = '';
        const text = li.textContent.replace(/^.*? /, '');
        li.innerHTML = `<i class="fa-solid fa-xmark"></i> ${text}`;
    });
}

// --- 2. KIBER-PAROL GENERATORI ---
const generatedPassword = document.getElementById('generatedPassword');
const lengthSlider = document.getElementById('lengthSlider');
const lengthValue = document.getElementById('lengthValue');
const generateBtn = document.getElementById('generateBtn');
const copyBtn = document.getElementById('copyBtn');
const genUpper = document.getElementById('genUpper');
const genLower = document.getElementById('genLower');
const genNum = document.getElementById('genNum');
const genSym = document.getElementById('genSym');

lengthSlider.addEventListener('input', (e) => { 
    lengthValue.textContent = e.target.value; 
});

function generateSecurePassword() {
    const length = parseInt(lengthSlider.value);
    let charset = '';
    if (genUpper.checked) charset += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (genLower.checked) charset += 'abcdefghijklmnopqrstuvwxyz';
    if (genNum.checked) charset += '0123456789';
    if (genSym.checked) charset += '!@#$%^&*()_+-=[]{}|;:,.<>?';

    if (!charset) {
        showToast("Kamida bitta belgi turini tanlang!");
        return;
    }

    const randomBuffer = new Uint32Array(length);
    window.crypto.getRandomValues(randomBuffer);
    let password = '';
    for (let i = 0; i < length; i++) {
        password += charset[randomBuffer[i] % charset.length];
    }
    generatedPassword.value = password;
}

generateBtn.addEventListener('click', generateSecurePassword);

copyBtn.addEventListener('click', () => {
    if (!generatedPassword.value) return;
    navigator.clipboard.writeText(generatedPassword.value);
    showToast("Parol buferga nusxalandi!");
});

// --- 3. PHISHING URL SCANNER ---
const urlForm = document.getElementById('urlForm');
const urlInput = document.getElementById('urlInput');
const urlResult = document.getElementById('urlResult');

urlForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const url = urlInput.value.trim().toLowerCase();
    urlResult.classList.remove('hidden');
    urlResult.className = 'result-box';
    urlResult.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Havola tahlil qilinmoqda...';

    setTimeout(() => {
        let risks = [];
        if (!url.startsWith('https://')) {
            risks.push("HTTPS shifrlash sertifikati mavjud emas (xavfli).");
        }
        if (url.includes('free') || url.includes('bonus') || url.includes('login-') || url.includes('verify') || url.includes('secure-') || url.includes('account-')) {
            risks.push("Havolada shubhali kalit so'zlar (bonus, login, free, verify, secure) mavjud — bu phishing belgisi.");
        }
        if ((url.match(/\./g) || []).length > 3) {
            risks.push("Haddan tashqari ko'p subdomenlar ishlatilgan (typosquatting xavfi).");
        }

        if (risks.length > 0) {
            urlResult.className = 'result-box danger';
            urlResult.innerHTML = `<strong><i class="fa-solid fa-triangle-exclamation"></i> XAVF ANIQLANDI!</strong><br><ul>` + risks.map(r => `<li>• ${r}</li>`).join('') + `</ul>`;
        } else {
            urlResult.className = 'result-box safe';
            urlResult.innerHTML = `<strong><i class="fa-solid fa-circle-check"></i> HAVOLA XAVFSIZ KO'RINADI</strong><br>Aniq fishing imzolari yoki shubhali belgilar topilmadi.`;
        }
    }, 800);
});

// --- 4. IP / DOMAIN LOOKUP ---
const ipForm = document.getElementById('ipForm');
const ipInput = document.getElementById('ipInput');
const ipResult = document.getElementById('ipResult');

ipForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = ipInput.value.trim();
    ipResult.classList.remove('hidden');
    ipResult.className = 'result-box';
    ipResult.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Tarmoq bazasidan so\'rov yuborilmoqda...';

    try {
        const response = await fetch(`https://ip-api.com/json/${query}`);
        const data = await response.json();

        if (data.status === 'success') {
            ipResult.className = 'result-box safe';
            ipResult.innerHTML = `
                <strong><i class="fa-solid fa-circle-info"></i> TARMOQ MA'LUMOTLARI TOPILDI:</strong><br>
                • <strong>IP / Domen:</strong> ${data.query}<br>
                • <strong>Mamlakat:</strong> ${data.country} (${data.countryCode})<br>
                • <strong>Shahar:</strong> ${data.city || 'Noma\'lum'}<br>
                • <strong>Provayder (ISP):</strong> ${data.isp}<br>
                • <strong>Geografik Koordinatalar:</strong> ${data.lat}, ${data.lon}
            `;
        } else {
            ipResult.className = 'result-box danger';
            ipResult.innerHTML = `<strong><i class="fa-solid fa-xmark"></i> Xatolik:</strong> Bunday IP-manzil yoki domen topilmadi yoki so'rov amalga oshmadi.`;
        }
    } catch (err) {
        ipResult.className = 'result-box danger';
        ipResult.innerHTML = `<strong><i class="fa-solid fa-triangle-exclamation"></i> Tarmoq xatoligi:</strong> Ma'lumotlarni olish imkoni bo'lmadi.`;
    }
});

// --- TOAST NOTIFICATION ---
function showToast(message) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.classList.remove('hidden');
    setTimeout(() => { 
        toast.classList.add('hidden'); 
    }, 2500);
}

// Dastlabki ishga tushirishda parolni generatsiya qilish
generateSecurePassword();