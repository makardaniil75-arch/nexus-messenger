<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <meta name="theme-color" content="#121212">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <title>Nexus Messenger · 6.2</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; font-family: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; -webkit-tap-highlight-color: transparent; }
    html, body { height: 100%; width: 100%; overflow: hidden; overscroll-behavior: none; }
    body { background: #000; display: flex; justify-content: center; align-items: center; margin: 0; position: fixed; inset: 0; }
    .app { width: 100vw; height: 100vh; height: 100dvh; background: #121212; overflow: hidden; position: relative; display: flex; flex-direction: column; padding-top: env(safe-area-inset-top); padding-bottom: env(safe-area-inset-bottom); }

    .screen { display: none; flex-direction: column; flex: 1; padding: 24px 22px 100px; overflow-y: auto; animation: fadeIn 0.25s ease; -webkit-overflow-scrolling: touch; }
    .screen.active { display: flex; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

    #screen-phone { background: linear-gradient(165deg, #121212 0%, #1a1a1a 55%, #222 100%); position: relative; justify-content: center; padding-bottom: 24px; }
    #screen-phone::before { content: ''; position: absolute; inset: 0; background-image: radial-gradient(circle at 20% 30%, rgba(108,140,255,0.15), transparent 45%), radial-gradient(circle at 80% 70%, rgba(180,100,255,0.12), transparent 45%); pointer-events: none; }
    #screen-phone > * { position: relative; z-index: 1; }
    .brand-badge { width: 84px; height: 84px; border-radius: 26px; background: linear-gradient(135deg, #6c8cff 0%, #b46cff 100%); display: flex; align-items: center; justify-content: center; font-size: 44px; margin-bottom: 20px; box-shadow: 0 20px 50px -12px rgba(108,140,255,0.55); }
    #t-login-title { font-size: 34px; background: linear-gradient(135deg, #fff 0%, #b4c2ff 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }

    h2 { color: #fff; font-weight: 700; font-size: 26px; margin-bottom: 6px; letter-spacing: -0.03em; }
    .sub { color: #8a8a8a; font-size: 15px; margin-bottom: 28px; line-height: 1.45; }
    input { width: 100%; padding: 16px 18px; background: #1e1e1e; border: 1.5px solid #2a2a2a; border-radius: 16px; color: #fff; font-size: 16px; outline: none; margin-bottom: 14px; transition: border 0.15s; }
    input:focus { border-color: #6c8cff; background: #222; }
    input::placeholder { color: #555; }
    .btn { background: linear-gradient(135deg, #6c8cff, #5b7cfa); border: none; color: #fff; font-weight: 700; font-size: 16px; padding: 16px; border-radius: 16px; cursor: pointer; width: 100%; margin-top: 6px; box-shadow: 0 8px 20px -6px rgba(108,140,255,0.5); transition: transform 0.1s; }
    .btn:active { transform: scale(0.98); }
    .btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }
    .btn-outline { background: transparent; border: 1.5px solid #2a2a2a; color: #b0b0b0; box-shadow: none; }
    .btn-danger { background: linear-gradient(135deg, #ff5c5c, #e03e3e); box-shadow: 0 8px 20px -6px rgba(255,92,92,0.5); }
    .btn-warn { background: linear-gradient(135deg, #f59e0b, #d97706); box-shadow: 0 8px 20px -6px rgba(245,158,11,0.5); }
    .btn-sm { padding: 10px 12px; font-size: 13px; border-radius: 12px; margin: 0; width: auto; }
    .link-btn { background: none; border: none; color: #6c8cff; font-size: 15px; font-weight: 600; cursor: pointer; padding: 8px 4px; }
    .code-badge { position: absolute; top: calc(20px + env(safe-area-inset-top)); right: 22px; background: #1e1e1e; padding: 10px 18px; border-radius: 40px; font-size: 15px; color: #a0b0ff; border: 1.5px solid #3b4b6b; font-family: monospace; letter-spacing: 2px; z-index: 10; font-weight: 600; }

    .phone-row { display: flex; gap: 8px; margin-bottom: 14px; }
    .country-selector { display: flex; align-items: center; gap: 8px; background: #1e1e1e; border: 1.5px solid #2a2a2a; border-radius: 16px; padding: 0 14px; cursor: pointer; flex-shrink: 0; min-width: 110px; height: 54px; transition: border-color 0.15s; }
    .country-selector:active { border-color: #6c8cff; }
    .country-selector .flag { font-size: 22px; line-height: 1; }
    .country-selector .code { color: #fff; font-weight: 600; font-size: 15px; }
    .country-selector .caret { color: #666; font-size: 11px; margin-left: auto; }
    .phone-row input { margin-bottom: 0; flex: 1; }

    .avatar-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 16px 0; }
    .avatar-option { aspect-ratio: 1/1; border-radius: 50%; background: #1e1e1e; display: flex; align-items: center; justify-content: center; font-size: 32px; cursor: pointer; border: 3px solid transparent; transition: border 0.15s; }
    .avatar-option.selected { border-color: #6c8cff; background: #2a2a2a; }

    .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; }
    .header h2 { margin: 0; }
    .search-bar { display: flex; align-items: center; background: #1e1e1e; border-radius: 16px; padding: 12px 16px; margin-bottom: 18px; border: 1.5px solid #2a2a2a; }
    .search-bar span { color: #666; font-size: 17px; margin-right: 10px; }
    .search-bar input { background: transparent; border: none; padding: 0; margin: 0; font-size: 15px; flex: 1; }
    .chat-list { display: flex; flex-direction: column; gap: 2px; flex: 1; overflow-y: auto; }
    .chat-item { display: flex; align-items: center; padding: 12px 10px; border-radius: 16px; cursor: pointer; }
    .chat-item:active { background: #1e1e1e; }
    .chat-avatar { width: 52px; height: 52px; border-radius: 50%; background: #2a2a2a; display: flex; align-items: center; justify-content: center; font-size: 26px; margin-right: 14px; position: relative; overflow: hidden; flex-shrink: 0; }
    .online-dot { position: absolute; bottom: 2px; right: 2px; width: 12px; height: 12px; background: #38d39f; border-radius: 50%; border: 2px solid #121212; }
    .chat-info { flex: 1; min-width: 0; }
    .chat-name { color: #fff; font-weight: 600; font-size: 16px; margin-bottom: 3px; display: flex; justify-content: space-between; }
    .chat-last { color: #8a8a8a; font-size: 13.5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .chat-time { font-size: 11.5px; color: #666; }

    .empty-state { display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px 20px; text-align: center; color: #666; }
    .empty-state .es-icon { font-size: 56px; margin-bottom: 16px; opacity: 0.6; }
    .empty-state .es-title { color: #aaa; font-size: 17px; font-weight: 600; margin-bottom: 8px; }
    .empty-state .es-text { font-size: 14px; line-height: 1.5; }

    .bottom-nav { display: flex; justify-content: space-around; align-items: center; position: absolute; bottom: 0; left: 0; right: 0; background: rgba(12, 17, 27, 0.95); backdrop-filter: blur(12px); border-top: 1px solid #1a2133; border-top-left-radius: 30px; border-top-right-radius: 30px; box-shadow: 0 -4px 20px rgba(0,0,0,0.4); padding: 10px 0 14px; padding-bottom: calc(14px + env(safe-area-inset-bottom)); margin-top: auto; flex-shrink: 0; }
    .nav-item { display: flex; flex-direction: column; align-items: center; gap: 4px; background: none; border: none; color: #5a657e; font-size: 11px; font-weight: 600; cursor: pointer; padding: 6px 20px; border-radius: 20px; transition: all 0.15s; min-width: 70px; }
    .nav-item.active { color: #fff; background: #1a2133; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
    .nav-icon { font-size: 21px; line-height: 1; }

    .chat-screen { display: none; flex-direction: column; flex: 1; position: absolute; inset: 0; background: #121212; z-index: 20; padding: 20px; padding-top: calc(20px + env(safe-area-inset-top)); padding-bottom: calc(20px + env(safe-area-inset-bottom)); }
    .chat-screen.active { display: flex; }
    .chat-header { display: flex; align-items: center; margin-bottom: 14px; gap: 10px; border-bottom: 1px solid #2a2a2a; padding-bottom: 12px; }
    .back-btn { background: #1e1e1e; border: none; color: #6c8cff; font-size: 20px; cursor: pointer; width: 38px; height: 38px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .chat-header .name { color: #fff; font-weight: 700; font-size: 17px; flex: 1; }
    .messages { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 8px; padding-bottom: 12px; }
    .msg { max-width: 82%; padding: 11px 15px; border-radius: 20px; font-size: 15px; line-height: 1.4; word-wrap: break-word; position: relative; animation: popIn 0.18s ease; }
    @keyframes popIn { from { transform: scale(0.92); opacity: 0; } to { transform: scale(1); opacity: 1; } }
    .msg.bot { background: #2a2a2a; color: #e1e1e1; align-self: flex-start; border-bottom-left-radius: 6px; }
    .msg.user { background: linear-gradient(135deg, #6c8cff, #5b7cfa); color: #fff; align-self: flex-end; border-bottom-right-radius: 6px; }
    .msg.typing { background: #2a2a2a; color: #8a8a8a; display: flex; align-items: center; gap: 6px; }
    .msg .msg-author { font-size: 11px; color: #8a8a8a; margin-bottom: 3px; }
    .dot-typing { width: 6px; height: 6px; background: #6c8cff; border-radius: 50%; animation: blink 1.2s infinite; }
    .dot-typing:nth-child(2) { animation-delay: 0.2s; }
    .dot-typing:nth-child(3) { animation-delay: 0.4s; }
    @keyframes blink { 0%,80%,100% { opacity: 0.3; } 40% { opacity: 1; } }
    .input-row { display: flex; gap: 8px; margin-top: auto; padding-top: 12px; border-top: 1px solid #2a2a2a; }
    .input-row input { margin: 0; flex: 1; border-radius: 22px; }
    .input-row .btn { width: auto; padding: 14px 18px; margin: 0; font-size: 18px; border-radius: 50%; }

    #screen-settings { background: #121212; padding-top: 10px; }
    .profile-top { display: flex; flex-direction: column; align-items: center; padding: 20px 0 28px 0; gap: 12px; }
    .profile-avatar-big { width: 100px; height: 100px; border-radius: 50%; background: #1e1e1e; border: 3px solid #2a2a2a; display: flex; align-items: center; justify-content: center; font-size: 48px; cursor: pointer; overflow: hidden; position: relative; flex-shrink: 0; transition: transform 0.12s, border-color 0.15s; }
    .profile-avatar-big:active { transform: scale(0.96); }
    .profile-avatar-big img { width: 100%; height: 100%; object-fit: cover; }
    .profile-avatar-big::after { content: '📷'; position: absolute; bottom: 0; right: 0; background: #6c8cff; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; border: 3px solid #121212; }
    .profile-top-name { color: #fff; font-weight: 700; font-size: 22px; text-align: center; }
    .profile-top-sub { color: #6a6a6a; font-size: 13px; text-align: center; }

    .settings-video-wrap { position: relative; width: 100%; aspect-ratio: 16/7; border-radius: 20px; overflow: hidden; margin-bottom: 8px; background: linear-gradient(135deg,#1a2133,#2a1a3e); border: 1px solid #2a2a2a; }
    .settings-video-wrap video, .settings-video-wrap img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .settings-video-wrap .vid-empty { width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #666; font-size: 13px; gap: 6px; }
    .banner-edit-btn { position: absolute; top: 10px; left: 10px; background: rgba(0,0,0,0.6); border: 1px solid #444; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; cursor: pointer; z-index: 5; color: #fff; }
    .banner-clear-btn { position: absolute; top: 10px; right: 10px; background: rgba(255,92,92,0.85); border: none; height: 40px; padding: 0 14px; border-radius: 20px; display: none; align-items: center; justify-content: center; color: #fff; font-size: 12px; cursor: pointer; z-index: 5; font-weight: 600; }
    .banner-clear-btn.show { display: flex; }

    .settings-menu { display: flex; flex-direction: column; background: #1c1c1e; border-radius: 16px; overflow: hidden; margin-bottom: 20px; }
    .settings-row { display: flex; align-items: center; gap: 14px; padding: 14px 16px; cursor: pointer; border-bottom: 1px solid #2a2a2a; transition: background 0.15s; }
    .settings-row:active { background: #2a2a2a; }
    .settings-row:last-child { border-bottom: none; }
    .settings-icon { width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 20px; flex-shrink: 0; color: #fff; }
    .icon-account { background: #3b82f6; }
    .icon-chats { background: #f59e0b; }
    .icon-privacy { background: #22c55e; }
    .icon-notify { background: #ef4444; }
    .icon-data { background: #3b82f6; }
    .icon-folders { background: #3b82f6; }
    .icon-devices { background: #0ea5e9; }
    .icon-battery { background: #f97316; }
    .icon-admin { background: #6c8cff; }
    .settings-text { flex: 1; }
    .settings-title { color: #fff; font-size: 16px; font-weight: 500; }
    .settings-desc { color: #8a8a8a; font-size: 13px; margin-top: 2px; }
    .settings-arrow { color: #444; font-size: 16px; margin-left: 10px; }

    .subscreen { display: none; flex-direction: column; flex: 1; position: absolute; inset: 0; background: #121212; z-index: 25; padding: 20px; padding-top: calc(20px + env(safe-area-inset-top)); padding-bottom: calc(20px + env(safe-area-inset-bottom)); overflow-y: auto; }
    .subscreen.active { display: flex; }
    .sub-header { display: flex; align-items: center; gap: 10px; margin-bottom: 20px; }
    .sub-header h3 { color: #fff; font-size: 20px; flex: 1; }

    .toggle-row { display: flex; align-items: center; justify-content: space-between; padding: 16px; background: #1c1c1e; border-radius: 16px; margin-bottom: 10px; }
    .toggle-row .ttext { color: #fff; font-size: 16px; }
    .switch { position: relative; width: 50px; height: 28px; flex-shrink: 0; }
    .switch input { opacity: 0; width: 0; height: 0; }
    .slider { position: absolute; cursor: pointer; inset: 0; background: #333; border-radius: 28px; transition: 0.2s; }
    .slider::before { content: ''; position: absolute; height: 22px; width: 22px; left: 3px; bottom: 3px; background: #fff; border-radius: 50%; transition: 0.2s; }
    .switch input:checked + .slider { background: #6c8cff; }
    .switch input:checked + .slider::before { transform: translateX(22px); }

    .version-footer { color: #444; font-size: 12px; text-align: center; padding: 16px 0; user-select: none; cursor: pointer; }
    .toast { position: absolute; bottom: 90px; left: 50%; transform: translateX(-50%) translateY(20px); background: #2a2a2a; color: #fff; padding: 12px 20px; border-radius: 30px; font-size: 14px; font-weight: 500; opacity: 0; pointer-events: none; transition: all 0.25s; z-index: 300; max-width: 90%; text-align:center; }
    .toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

    .modal-overlay { display: none; position: absolute; inset: 0; background: rgba(0,0,0,0.8); z-index: 200; align-items: center; justify-content: center; padding: 20px; }
    .modal-overlay.show { display: flex; }
    .modal-content { background: #1c1c1e; border-radius: 20px; padding: 24px; width: 100%; max-width: 340px; border: 1px solid #2a2a2a; max-height: 85vh; display: flex; flex-direction: column; }
    .modal-content h3 { color: #fff; margin-bottom: 16px; font-size: 18px; text-align: center; }

    .country-modal-list { overflow-y: auto; max-height: 50vh; margin-bottom: 14px; }
    .country-modal-item { display: flex; align-items: center; gap: 12px; padding: 12px 10px; border-radius: 12px; cursor: pointer; }
    .country-modal-item:active { background: #2a2a2a; }
    .country-modal-item .flag { font-size: 24px; }
    .country-modal-item .cname { color: #fff; flex: 1; font-size: 15px; }
    .country-modal-item .ccode { color: #8a8a8a; font-family: monospace; font-size: 14px; }

    .admin-user-card { background: #1e1e1e; border: 1px solid #2a2a2a; border-radius: 16px; padding: 14px; margin-bottom: 10px; display: flex; flex-direction: column; gap: 10px; }
    .admin-user-head { display: flex; align-items: center; gap: 12px; }
    .admin-user-head .au-avatar { width: 46px; height: 46px; border-radius: 50%; background: #2a2a2a; display: flex; align-items: center; justify-content: center; font-size: 22px; overflow: hidden; flex-shrink: 0; }
    .admin-user-head .au-info { flex: 1; min-width: 0; }
    .admin-user-head .au-name { color: #fff; font-weight: 700; font-size: 15px; display: flex; gap: 6px; flex-wrap: wrap; align-items: center; }
    .admin-user-head .au-phone { color: #8a8a8a; font-size: 12.5px; margin-top: 2px; word-break: break-all; }
    .badge { padding: 2px 8px; border-radius: 20px; font-size: 10.5px; font-weight: 700; }
    .badge-banned { background: rgba(255,92,92,0.2); color: #ff8080; }
    .badge-kicked { background: rgba(245,166,35,0.2); color: #f5b944; }
    .badge-online { background: rgba(56,211,159,0.2); color: #38d39f; }
    .badge-admin { background: rgba(108,140,255,0.2); color: #93a8ff; }
    .admin-actions { display: flex; flex-wrap: wrap; gap: 8px; }

    .profile-banner-wrap { position: relative; width: 100%; aspect-ratio: 16/7; border-radius: 20px; overflow: hidden; margin-bottom: 16px; background: #1e1e1e; border: 1px solid #2a2a2a; }
    .profile-banner-wrap .banner-media { width: 100%; height: 100%; object-fit: cover; display: none; }
    .profile-banner-wrap .banner-empty { width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #666; font-size: 13px; }

    .profile-bg-preview { width: 100%; aspect-ratio: 16/9; border-radius: 16px; background-size: cover; background-position: center; border: 1px solid #2a2a2a; margin-bottom: 12px; display: flex; align-items: center; justify-content: center; color: #666; font-size: 13px; }
    .bg-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 12px; }
    .bg-option { aspect-ratio: 1/1; border-radius: 12px; cursor: pointer; border: 3px solid transparent; background-size: cover; background-position: center; }
    .bg-option.selected { border-color: #6c8cff; }
  </style>
</head>
<body>
<div class="app" id="app">

  <!-- ТЕЛЕФОН -->
  <div class="screen active" id="screen-phone">
    <div class="brand-badge">💬</div>
    <h2 id="t-login-title">Nexus</h2>
    <p class="sub" id="phone-sub">Войдите по номеру телефона, чтобы начать общение</p>
    <div class="phone-row">
      <div class="country-selector" id="country-selector">
        <span class="flag" id="selected-flag">🇷🇺</span>
        <span class="code" id="selected-code">+7</span>
        <span class="caret">▼</span>
      </div>
      <input type="tel" id="phone-input" placeholder="999 123-45-67">
    </div>
    <button class="btn" id="btn-get-code">Получить код</button>
    <div id="saved-account-hint" style="display:none; margin-top:16px; text-align:center;">
      <button class="link-btn" id="btn-restore-account">↩ Войти в сохранённый аккаунт</button>
    </div>
  </div>

  <!-- МОДАЛКА СТРАНЫ -->
  <div class="modal-overlay" id="modal-country">
    <div class="modal-content">
      <h3>Выберите страну</h3>
      <div class="search-bar" style="margin-bottom:12px;"><span>🔍</span><input type="text" id="country-search" placeholder="Поиск страны..."></div>
            <div class="country-modal-list" id="country-list"></div>
      <button class="btn btn-outline" id="btn-close-country" style="margin:0;">Закрыть</button>
    </div>
  </div>

  <!-- КОД (РЕАЛЬНАЯ SMS) -->
  <div class="screen" id="screen-code">
    <div style="margin-top: 40px;">
      <h2>Введите код</h2>
      <p class="sub">Мы отправили SMS с кодом на ваш номер. Введите его ниже.</p>
    </div>
    <input type="text" id="code-input" placeholder="000000" maxlength="6" inputmode="numeric" style="text-align:center; font-size:22px; letter-spacing:10px; font-weight:700;">
    <button class="btn" id="btn-verify-code">Продолжить</button>
    <button class="btn btn-outline" id="btn-resend-code" disabled style="margin-top:10px;">Отправить снова (60)</button>
    <button class="link-btn" id="btn-back-phone" style="margin-top:10px;">← Изменить номер</button>
  </div>

  <!-- ПАРОЛЬ -->
  <div class="screen" id="screen-password">
    <h2>Введите пароль</h2>
    <p class="sub">Аккаунт защищён паролем</p>
    <input type="password" id="password-input" placeholder="Пароль">
    <button class="btn" id="btn-verify-password">Войти</button>
    <button class="btn btn-outline" id="btn-forgot-pass" style="margin-top:10px;">Забыли пароль? Сбросить</button>
    <button class="link-btn" id="btn-back-phone-2" style="margin-top:8px;">← Назад</button>
  </div>

  <!-- ПРОФИЛЬ (регистрация) -->
  <div class="screen" id="screen-profile">
    <h2>Профиль</h2>
    <p class="sub">Введите настоящее имя и номер телефона — только после этого появятся чаты с реальными людьми</p>
    <input type="text" id="first-name" placeholder="Имя">
    <input type="text" id="last-name" placeholder="Фамилия">
    <div class="phone-row">
      <div class="country-selector" id="country-selector-2">
        <span class="flag" id="selected-flag-2">🇷🇺</span>
        <span class="code" id="selected-code-2">+7</span>
        <span class="caret">▼</span>
      </div>
      <input type="tel" id="real-phone" placeholder="Ваш настоящий номер">
    </div>
    <div class="avatar-grid" id="avatar-grid"></div>
    <button class="btn" id="btn-finish-profile">Начать общение</button>
  </div>

  <!-- ГЛАВНАЯ -->
  <div class="screen" id="screen-main">
    <div class="header">
      <h2>Чаты</h2>
      <div style="display:flex; gap:4px;">
        <button class="link-btn" id="btn-new-chat" style="font-size:24px;">＋</button>
        <button class="link-btn" id="btn-settings-top" style="font-size:22px;">⚙️</button>
      </div>
    </div>
    <div class="search-bar"><span>🔍</span><input type="text" id="search-chats" placeholder="Поиск людей и чатов..."></div>
    <div class="chat-list" id="chat-list"></div>

    <div class="bottom-nav">
      <button class="nav-item" id="nav-settings"><span class="nav-icon">⚙️</span><span>Настройки</span></button>
      <button class="nav-item active" id="nav-main"><span class="nav-icon">🏠</span><span>Главная</span></button>
      <button class="nav-item" id="nav-chats"><span class="nav-icon">💬</span><span>Чаты</span></button>
    </div>
  </div>

  <!-- НАСТРОЙКИ -->
  <div class="screen" id="screen-settings">
    <div class="header" style="margin-bottom: 8px;">
      <h2 style="font-size: 30px;">Настройки</h2>
      <button class="link-btn" id="btn-close-settings" style="font-size:24px;">✕</button>
    </div>

    <div class="settings-video-wrap" id="settings-video-wrap">
      <div class="vid-empty" id="sv-empty">🎬 Добавьте видео или фото<br><span style="font-size:11px;">нажмите 📷</span></div>
      <video id="sv-video" style="display:none;" autoplay muted loop playsinline></video>
      <img id="sv-img" style="display:none;" alt="">
      <button class="banner-edit-btn" id="sv-edit" title="Изменить">📷</button>
      <button class="banner-clear-btn" id="sv-clear">Удалить</button>
    </div>
    <input type="file" id="sv-file" accept="video/*,image/*" style="display:none;">

    <div class="profile-top" style="padding-top:12px;">
      <div class="profile-avatar-big" id="settings-avatar-btn">
        <span id="settings-avatar-emoji">👤</span>
        <img id="settings-avatar-img" style="display:none;" alt="">
      </div>
      <div>
        <div class="profile-top-name" id="settings-name">Пользователь</div>
        <div class="profile-top-sub" id="settings-phone-sub">нажмите на фото, чтобы изменить</div>
      </div>
    </div>
    <input type="file" id="avatar-file-input" accept="image/*" style="display:none;">

    <div class="settings-menu">
      <div class="settings-row" data-setting="account">
        <div class="settings-icon icon-account">👤</div>
        <div class="settings-text"><div class="settings-title">Аккаунт</div><div class="settings-desc">Имя, телефон, фото профиля</div></div>
        <div class="settings-arrow">›</div>
      </div>
      <div class="settings-row" data-setting="chats">
        <div class="settings-icon icon-chats">💬</div>
        <div class="settings-text"><div class="settings-title">Чаты</div><div class="settings-desc">Обои, тема, размер текста</div></div>
        <div class="settings-arrow">›</div>
      </div>
      <div class="settings-row" data-setting="privacy">
        <div class="settings-icon icon-privacy">🔒</div>
        <div class="settings-text"><div class="settings-title">Приватность</div><div class="settings-desc">Кто видит ваш профиль</div></div>
        <div class="settings-arrow">›</div>
      </div>
      <div class="settings-row" data-setting="notify">
        <div class="settings-icon icon-notify">🔔</div>
        <div class="settings-text"><div class="settings-title">Уведомления</div><div class="settings-desc">Звуки, вибрация, push</div></div>
        <div class="settings-arrow">›</div>
      </div>
      <div class="settings-row" data-setting="security">
        <div class="settings-icon" style="background:#8b5cf6;">🔐</div>
        <div class="settings-text"><div class="settings-title">Безопасность</div><div class="settings-desc">Пароль, вход по коду</div></div>
        <div class="settings-arrow">›</div>
      </div>
      <div class="settings-row" data-setting="data">
        <div class="settings-icon icon-data">📦</div>
        <div class="settings-text"><div class="settings-title">Данные и память</div><div class="settings-desc">Хранилище, кэш</div></div>
        <div class="settings-arrow">›</div>
      </div>
      <div class="settings-row" data-setting="folders">
        <div class="settings-icon icon-folders">📁</div>
        <div class="settings-text"><div class="settings-title">Папки с чатами</div><div class="settings-desc">Сортировка диалогов</div></div>
        <div class="settings-arrow">›</div>
      </div>
      <div class="settings-row" data-setting="devices">
        <div class="settings-icon icon-devices">📱</div>
        <div class="settings-text"><div class="settings-title">Устройства</div><div class="settings-desc">Активные сеансы</div></div>
        <div class="settings-arrow">›</div>
      </div>
      <div class="settings-row" data-setting="battery">
        <div class="settings-icon icon-battery">🔋</div>
        <div class="settings-text"><div class="settings-title">Батарея и память</div><div class="settings-desc">Энергосбережение</div></div>
        <div class="settings-arrow">›</div>
      </div>
    </div>

    <button class="btn btn-danger" id="btn-logout" style="margin-bottom:16px;">Выйти из аккаунта</button>

    <div class="version-footer" id="version-footer">Nexus Messenger · v6.2</div>
  </div>

  <!-- ПОДЭКРАН: ПРОФИЛЬ -->
  <div class="subscreen" id="sub-account">
    <div class="sub-header"><button class="back-btn" data-close-sub="sub-account">←</button><h3>Профиль</h3></div>

    <div class="profile-banner-wrap" id="prof-banner-wrap">
      <img class="banner-media" id="prof-banner-img" alt="">
      <video class="banner-media" id="prof-banner-video" muted loop playsinline></video>
      <div class="banner-empty" id="prof-banner-empty">🖼 Баннер<br><span style="font-size:11px;">нажмите 📷</span></div>
      <button class="banner-edit-btn" id="prof-banner-edit">📷</button>
      <button class="banner-clear-btn" id="prof-banner-clear">Удалить</button>
    </div>
    <input type="file" id="prof-banner-file" accept="video/*,image/*" style="display:none;">

    <div class="profile-top" style="padding:0 0 16px 0;">
      <div class="profile-avatar-big" id="account-avatar-btn">
        <span id="account-avatar-emoji">👤</span>
        <img id="account-avatar-img" style="display:none;" alt="">
      </div>
    </div>
    <input type="file" id="account-avatar-file" accept="image/*" style="display:none;">

    <label class="sub">Имя</label>
    <input type="text" id="acc-first-name" placeholder="Имя">
    <label class="sub">Фамилия</label>
    <input type="text" id="acc-last-name" placeholder="Фамилия">

    <label class="sub">Фон профиля</label>
    <div class="profile-bg-preview" id="profile-bg-preview">Без фона</div>
    <div class="bg-grid" id="bg-grid"></div>
    <input type="file" id="bg-file" accept="image/*" style="display:none;">
    <button class="btn btn-outline" id="btn-upload-bg" style="margin-bottom:14px;">Загрузить свой фон</button>
    <button class="btn btn-outline" id="btn-clear-bg" style="margin-bottom:14px;">Убрать фон</button>

    <button class="btn" id="btn-save-account">Сохранить</button>
  </div>

  <!-- ПОДЭКРАН: УВЕДОМЛЕНИЯ -->
  <div class="subscreen" id="sub-notify">
    <div class="sub-header"><button class="back-btn" data-close-sub="sub-notify">←</button><h3>Уведомления</h3></div>
    <div class="toggle-row"><span class="ttext">Уведомления включены</span><label class="switch"><input type="checkbox" id="toggle-notify"><span class="slider"></span></label></div>
    <div class="toggle-row"><span class="ttext">Звук сообщений</span><label class="switch"><input type="checkbox" id="toggle-sound" checked><span class="slider"></span></label></div>
    <div class="toggle-row"><span class="ttext">Вибрация</span><label class="switch"><input type="checkbox" id="toggle-vibrate" checked><span class="slider"></span></label></div>
    <p class="sub" style="margin-top:10px;">Настройки сохраняются автоматически.</p>
  </div>

  <!-- ПОДЭКРАН: БЕЗОПАСНОСТЬ -->
  <div class="subscreen" id="sub-security">
    <div class="sub-header"><button class="back-btn" data-close-sub="sub-security">←</button><h3>Безопасность</h3></div>
    <p class="sub" id="security-status">Пароль не установлен</p>
    <input type="password" id="new-password" placeholder="Новый пароль">
    <input type="password" id="confirm-password" placeholder="Повторите пароль">
    <button class="btn" id="btn-set-password">Установить пароль</button>
    <button class="btn btn-danger" id="btn-remove-password" style="display:none; margin-top:10px;">Удалить пароль</button>
  </div>

  <!-- ПОДЭКРАН: ВВОД ПАРОЛЯ АДМИНА -->
  <div class="subscreen" id="sub-admin-lock">
    <div class="sub-header"><button class="back-btn" data-close-sub="sub-admin-lock">←</button><h3>Админ-панель</h3></div>
    <p class="sub">Введите секретный пароль</p>
    <input type="password" id="admin-pass-input" placeholder="Пароль" inputmode="numeric">
    <button class="btn" id="btn-admin-login">Войти</button>
  </div>

  <!-- ПОДЭКРАН: АДМИН-ПАНЕЛЬ -->
  <div class="subscreen" id="sub-admin">
    <div class="sub-header"><button class="back-btn" data-close-sub="sub-admin">←</button><h3>Админ-панель</h3></div>
    <p class="sub">Управление пользователями</p>
    <div id="admin-users-list"></div>
  </div>

  <!-- ПОДЭКРАН: ЗАГЛУШКА -->
  <div class="subscreen" id="sub-generic">
    <div class="sub-header"><button class="back-btn" data-close-sub="sub-generic">←</button><h3 id="generic-title">Раздел</h3></div>
    <p class="sub">Этот раздел в разработке. Скоро здесь появятся настройки.</p>
  </div>

  <!-- ЧАТ -->
  <div class="chat-screen" id="chat-screen">
    <div class="chat-header">
      <button class="back-btn" id="btn-back-chat">←</button>
      <div class="name" id="chat-title">Чат</div>
    </div>
    <div class="messages" id="messages"></div>
    <div class="input-row">
      <input type="text" id="msg-input" placeholder="Сообщение...">
      <button class="btn" id="btn-send">➤</button>
    </div>
  </div>

  <!-- НОВЫЙ ЧАТ -->
  <div class="modal-overlay" id="modal-new-chat">
    <div class="modal-content" style="max-width:360px;">
      <h3>Новый чат</h3>
      <div class="search-bar" style="margin-bottom:12px;"><span>🔍</span><input type="text" id="new-chat-search" placeholder="Имя..."></div>
      <div id="new-chat-results" style="max-height:260px; overflow-y:auto; display:flex; flex-direction:column; gap:2px;"></div>
      <div style="display:flex; gap:8px; margin-top:14px;">
        <button class="btn btn-outline" id="btn-cancel-new-chat" style="margin:0;">Отмена</button>
        <button class="btn" id="btn-create-ai-chat" style="margin:0;">🤖 AI-чат</button>
      </div>
    </div>
  </div>

  <div class="toast" id="toast"></div>
</div>

<!-- Firebase SDK -->
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-auth-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-database-compat.js"></script>

<script>
/* ================= FIREBASE ================= */
const firebaseConfig = { databaseURL: "https://my-messager-d8953-default-rtdb.firebaseio.com/" };
firebase.initializeApp(firebaseConfig);
const db = firebase.database();
const auth = firebase.auth();

/* ================= СТРАНЫ ================= */
const COUNTRIES = [
  { flag:'🇷🇺', code:'+7',   name:'Россия',          iso:'ru', mask:'999 123-45-67' },
  { flag:'🇰🇿', code:'+7',   name:'Казахстан',       iso:'kz', mask:'999 123-45-67' },
  { flag:'🇧🇾', code:'+375', name:'Беларусь',        iso:'by', mask:'99 123-45-67' },
  { flag:'🇺🇦', code:'+380', name:'Украина',         iso:'ua', mask:'99 123-45-67' },
  { flag:'🇺🇸', code:'+1',   name:'США',             iso:'us', mask:'999 123-4567' },
  { flag:'🇬🇧', code:'+44',  name:'Великобритания',  iso:'gb', mask:'9999 123456' },
  { flag:'🇩🇪', code:'+49',  name:'Германия',        iso:'de', mask:'999 12345678' },
  { flag:'🇫🇷', code:'+33',  name:'Франция',         iso:'fr', mask:'9 12 34 56 78' },
  { flag:'🇹🇷', code:'+90',  name:'Турция',          iso:'tr', mask:'999 123 45 67' },
  { flag:'🇨🇳', code:'+86',  name:'Китай',           iso:'cn', mask:'999 1234 5678' },
  { flag:'🇯🇵', code:'+81',  name:'Япония',          iso:'jp', mask:'99 1234 5678' },
  { flag:'🇰🇷', code:'+82',  name:'Южная Корея',     iso:'kr', mask:'99 1234 5678' },
  { flag:'🇮🇳', code:'+91',  name:'Индия',           iso:'in', mask:'99999 12345' },
  { flag:'🇧🇷', code:'+55',  name:'Бразилия',        iso:'br', mask:'99 12345 6789' },
  { flag:'🇦🇺', code:'+61',  name:'Австралия',       iso:'au', mask:'999 123 456' }
];
let selectedCountry = COUNTRIES[0];
let selectedCountry2 = COUNTRIES[0];

function renderCountryList(query = '') {
  const q = query.trim().toLowerCase();
  const filtered = COUNTRIES.filter(c => c.name.toLowerCase().includes(q) || c.code.includes(q) || c.iso.includes(q));
  document.getElementById('country-list').innerHTML = filtered.map(c => `
    <div class="country-modal-item" data-iso="${c.iso}" data-code="${c.code}">
      <span class="flag">${c.flag}</span><span class="cname">${c.name}</span><span class="ccode">${c.code}</span>
    </div>`).join('') || '<div style="color:#666;text-align:center;padding:20px;">Не найдено</div>';
  document.querySelectorAll('.country-modal-item').forEach(el => {
    el.onclick = () => selectCountry(el.dataset.iso, el.dataset.code);
  });
}
function selectCountry(iso, code) {
  const c = COUNTRIES.find(x => x.iso === iso && x.code === code);
  if (!c) return;
  selectedCountry = c;
  document.getElementById('selected-flag').textContent = c.flag;
  document.getElementById('selected-code').textContent = c.code;
  document.getElementById('phone-input').placeholder = c.mask;
  document.getElementById('phone-input').value = '';
  document.getElementById('modal-country').classList.remove('show');
}
document.getElementById('country-selector').onclick = () => {
  renderCountryList('');
  document.getElementById('country-search').value = '';
  document.getElementById('modal-country').classList.add('show');
};
document.getElementById('country-selector-2').onclick = () => {
  renderCountryList('');
  document.getElementById('country-search').value = '';
  document.getElementById('modal-country').classList.add('show');
};
document.getElementById('btn-close-country').onclick = () => document.getElementById('modal-country').classList.remove('show');
document.getElementById('country-search').addEventListener('input', e => renderCountryList(e.target.value));
document.getElementById('modal-country').addEventListener('click', e => { if (e.target === document.getElementById('modal-country')) document.getElementById('modal-country').classList.remove('show'); });

/* ================= СОХРАНЕНИЕ ================= */
const SAVED_KEY = 'nexus_saved_account';
function getSavedAccount() {
  try { return JSON.parse(localStorage.getItem(SAVED_KEY) || 'null'); } catch { return null; }
}
function saveAccount(acc) { localStorage.setItem(SAVED_KEY, JSON.stringify(acc)); }
function hasPassword() { return !!localStorage.getItem('nexus_password'); }

/* ================= СОСТОЯНИЕ ================= */
let user = { name: 'Пользователь', emoji: '👤', avatar: null, profileBg: null, banner: null, bannerType: null, phone: '' };
let chats = [{ id: 'ai', name: 'Nexus AI', emoji: '🤖', isAI: true, messages: [{ from: 'bot', text: 'Привет! 👋 Я Nexus AI. Могу решать примеры: напиши «2*3» или «10/2»' }], lastTime: 'сейчас' }];
let currentChat = null;
let selectedAvatar = '👤';
let myUid = null;
let usersCache = {};
let blockedUsers = {};
let realChatsEnabled = false;
let confirmationResult = null;
let resendTimer = null;
const avatarEmojis = ['👤','🐺','🌸','🦊','🐱','🐼','🦁','🐸','🦄','🐙','🐧','🦉'];
const ADMIN_PASSWORD = '130816';

/* ================= УТИЛИТЫ ================= */
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
}
function toast(text) {
  const t = document.getElementById('toast');
  t.textContent = text;
  t.classList.add('show');
  clearTimeout(t._tm);
  t._tm = setTimeout(() => t.classList.remove('show'), 2200);
}
function uidFor(phone) { return 'u_' + btoa(unescape(encodeURIComponent(phone))).replace(/=/g, '').toLowerCase(); }

function restoreUserFromSaved(saved) {
  user.name = saved.name || 'Пользователь';
  user.emoji = saved.emoji || '👤';
  user.avatar = saved.avatar || null;
  user.profileBg = saved.profileBg || null;
  user.banner = saved.banner || null;
  user.bannerType = saved.bannerType || null;
  user.phone = saved.phone || '';
  myUid = saved.uid;
  realChatsEnabled = true;
  document.getElementById('settings-name').textContent = user.name;
  document.getElementById('settings-avatar-emoji').textContent = user.emoji;
  if (user.avatar) {
    const img = document.getElementById('settings-avatar-img');
    img.src = user.avatar; img.style.display = 'block';
    document.getElementById('settings-avatar-emoji').style.display = 'none';
  }
  document.getElementById('settings-phone-sub').textContent = user.phone || 'нажмите на фото, чтобы изменить';
}

/* ================= АВАТАРЫ ================= */
const avatarGrid = document.getElementById('avatar-grid');
avatarEmojis.forEach(e => {
  const d = document.createElement('div');
  d.className = 'avatar-option' + (e === selectedAvatar ? ' selected' : '');
  d.textContent = e;
  d.onclick = () => {
    selectedAvatar = e;
    document.querySelectorAll('.avatar-option').forEach(x => x.classList.remove('selected'));
    d.classList.add('selected');
  };
    avatarGrid.appendChild(d);
});

/* ================= ОТПРАВКА SMS ЧЕРЕЗ FIREBASE ================= */
function startResendTimer() {
  const btn = document.getElementById('btn-resend-code');
  let seconds = 60;
  btn.disabled = true;
  btn.textContent = `Отправить снова (${seconds})`;
  clearInterval(resendTimer);
  resendTimer = setInterval(() => {
    seconds--;
    if (seconds <= 0) {
      clearInterval(resendTimer);
      btn.disabled = false;
      btn.textContent = 'Отправить снова';
    } else {
      btn.textContent = `Отправить снова (${seconds})`;
    }
  }, 1000);
}

function sendSmsCode(fullPhone) {
  if (!window.recaptchaVerifier) {
    window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier('btn-get-code', {
      'size': 'invisible'
    });
  }
  auth.signInWithPhoneNumber(fullPhone, window.recaptchaVerifier)
    .then((result) => {
      confirmationResult = result;
      document.getElementById('code-input').value = '';
      showScreen('screen-code');
      startResendTimer();
      toast('SMS с кодом отправлено на ' + fullPhone);
    })
    .catch((error) => {
      console.error('SMS error:', error);
      let msg = 'Ошибка отправки SMS';
      if (error.code === 'auth/too-many-requests') msg = 'Слишком много попыток. Попробуйте позже.';
      else if (error.code === 'auth/quota-exceeded') msg = 'Лимит SMS исчерпан. Попробуйте позже.';
      else if (error.code === 'auth/invalid-phone-number') msg = 'Неверный формат номера.';
      else if (error.code === 'auth/captcha-check-failed') msg = 'Ошибка проверки reCAPTCHA. Обновите страницу.';
      else msg = error.message || msg;
      toast(msg);
      if (window.recaptchaVerifier) {
        window.recaptchaVerifier.render().then((widgetId) => {
          grecaptcha.reset(widgetId);
        }).catch(() => {});
      }
    });
}

/* ================= ВХОД ================= */
document.getElementById('btn-get-code').onclick = () => {
  const phone = document.getElementById('phone-input').value.replace(/\D/g, '');
  if (!phone) return toast('Введите номер');
  const saved = getSavedAccount();
  const fullPhone = selectedCountry.code + phone;

  if (saved && saved.phone === fullPhone) {
    if (hasPassword()) {
      document.getElementById('password-input').value = '';
      showScreen('screen-password');
    } else {
      restoreUserFromSaved(saved);
      showScreen('screen-main');
      renderChats();
      listenUsers();
      listenIncomingMessages();
      toast('С возвращением, ' + user.name + '!');
    }
    return;
  }
  if (saved && saved.phone !== fullPhone) {
    toast('Сначала выйдите из текущего аккаунта (Настройки → Выйти)');
    return;
  }
  sendSmsCode(fullPhone);
};
document.getElementById('btn-back-phone').onclick = () => {
  clearInterval(resendTimer);
  showScreen('screen-phone');
};
document.getElementById('btn-back-phone-2').onclick = () => showScreen('screen-phone');

document.getElementById('btn-resend-code').onclick = () => {
  if (document.getElementById('btn-resend-code').disabled) return;
  const phone = document.getElementById('phone-input').value.replace(/\D/g, '');
  if (!phone) return toast('Введите номер');
  const fullPhone = selectedCountry.code + phone;
  sendSmsCode(fullPhone);
};

document.getElementById('btn-verify-code').onclick = () => {
  const input = document.getElementById('code-input').value.trim();
  if (!input || input.length < 6) return toast('Введите 6-значный код из SMS');
  if (!confirmationResult) return toast('Сначала запросите код');

  confirmationResult.confirm(input)
    .then(() => {
      clearInterval(resendTimer);
      if (hasPassword()) showScreen('screen-password');
      else showScreen('screen-profile');
    })
    .catch((error) => {
      console.error('Confirm error:', error);
      if (error.code === 'auth/invalid-verification-code') toast('Неверный код. Проверьте SMS.');
      else if (error.code === 'auth/code-expired') toast('Код истёк. Запросите новый.');
      else toast('Ошибка: ' + (error.message || 'неверный код'));
    });
};

/* ================= ПАРОЛЬ ================= */
document.getElementById('btn-verify-password').onclick = () => {
  const pass = document.getElementById('password-input').value;
  if (pass !== localStorage.getItem('nexus_password')) return toast('Неверный пароль');
  const saved = getSavedAccount();
  if (saved) {
    restoreUserFromSaved(saved);
    showScreen('screen-main');
    renderChats();
    listenUsers();
    listenIncomingMessages();
    toast('С возвращением, ' + user.name + '!');
    return;
  }
  showScreen('screen-main');
};
document.getElementById('btn-forgot-pass').onclick = () => {
  if (!confirm('Сбросить пароль? Вы сможете войти без пароля.')) return;
  localStorage.removeItem('nexus_password');
  toast('Пароль сброшен. Входим без пароля.');
  const saved = getSavedAccount();
  if (saved) {
    restoreUserFromSaved(saved);
    showScreen('screen-main');
    renderChats();
    listenUsers();
    listenIncomingMessages();
  } else {
    showScreen('screen-phone');
  }
};
document.getElementById('btn-restore-account').onclick = () => {
  const saved = getSavedAccount();
  if (!saved) return toast('Сохранённых аккаунтов нет');
  if (hasPassword()) {
    document.getElementById('phone-input').value = saved.phone.replace(saved.countryCode || '', '');
    document.getElementById('password-input').value = '';
    showScreen('screen-password');
  } else {
    restoreUserFromSaved(saved);
    showScreen('screen-main');
    renderChats();
    listenUsers();
    listenIncomingMessages();
    toast('С возвращением, ' + user.name + '!');
  }
};

/* ================= РЕГИСТРАЦИЯ ================= */
document.getElementById('btn-finish-profile').onclick = () => {
  const first = document.getElementById('first-name').value.trim();
  const last = document.getElementById('last-name').value.trim();
  const realPhone = document.getElementById('real-phone').value.replace(/\D/g, '');
  if (!first) return toast('Введите имя');
  if (!realPhone || realPhone.length < 6) return toast('Введите настоящий номер телефона');
  user.name = [first, last].filter(Boolean).join(' ');
  user.emoji = selectedAvatar;
  user.phone = selectedCountry2.code + realPhone;
  myUid = uidFor(user.phone);
  realChatsEnabled = true;

  document.getElementById('settings-name').textContent = user.name;
  document.getElementById('settings-avatar-emoji').textContent = user.emoji;
  document.getElementById('settings-phone-sub').textContent = user.phone;

  saveAccount({
    uid: myUid, name: user.name, emoji: user.emoji,
    phone: user.phone, countryCode: selectedCountry2.code,
    avatar: null, profileBg: null, banner: null, bannerType: null
  });

  db.ref('users/' + myUid).set({
    name: user.name, emoji: user.emoji, phone: user.phone,
    country: selectedCountry2.iso, online: true, lastSeen: Date.now()
  });

  showScreen('screen-main');
  renderChats();
  listenUsers();
  listenIncomingMessages();
  toast('Добро пожаловать в Nexus! 👋');
};

/* ================= ВЫХОД ================= */
document.getElementById('btn-logout').onclick = () => {
  if (!confirm('Выйти из аккаунта? Данные сохранятся, вы сможете войти снова.')) return;
  const saved = getSavedAccount();
  if (saved) {
    saved.name = user.name; saved.emoji = user.emoji;
    saved.avatar = user.avatar; saved.profileBg = user.profileBg;
    saved.banner = user.banner; saved.bannerType = user.bannerType;
    saveAccount(saved);
  }
  if (myUid) db.ref('users/' + myUid).update({ online: false });
  showScreen('screen-phone');
  document.getElementById('password-input').value = '';
  document.getElementById('phone-input').value = '';
  updateSavedHint();
  toast('Вы вышли. Аккаунт сохранён.');
};

function updateSavedHint() {
  const saved = getSavedAccount();
  document.getElementById('saved-account-hint').style.display = saved ? 'block' : 'none';
}

/* ================= ПОЛЬЗОВАТЕЛИ ================= */
function listenUsers() {
  if (!realChatsEnabled) return;
  db.ref('users').on('value', snap => {
    usersCache = snap.val() || {};
    Object.keys(usersCache).forEach(id => {
      if (id === myUid) return;
      const u = usersCache[id];
      if (u.banned) return;
      if (!chats.find(c => c.id === id)) chats.push({ id, name: u.name, emoji: u.emoji || '👤', messages: [], lastTime: '' });
    });
    renderChats();
    if (document.getElementById('sub-admin').classList.contains('active')) renderAdminUsers();
  });
}

/* ================= СПИСОК ЧАТОВ ================= */
function renderChats(filter = '') {
  const list = document.getElementById('chat-list');
  const q = filter.trim().toLowerCase();
  const filtered = chats.filter(c => c.name.toLowerCase().includes(q));
  if (!realChatsEnabled && filtered.length === 1) {
    list.innerHTML = `<div class="empty-state">
      <div class="es-icon">🔒</div>
      <div class="es-title">Чаты с людьми скрыты</div>
      <div class="es-text">Чтобы начать общение с реальными людьми, заполните профиль: имя и настоящий номер телефона.</div>
    </div>`;
    return;
  }
  list.innerHTML = filtered.map(c => {
    const last = c.messages.length ? c.messages[c.messages.length - 1].text : (c.isAI ? 'AI-ассистент' : 'Начните диалог');
    return `<div class="chat-item" data-id="${c.id}">
      <div class="chat-avatar">${c.emoji}${c.isAI ? '<span class="online-dot"></span>' : ''}</div>
      <div class="chat-info">
        <div class="chat-name"><span>${c.name}</span><span class="chat-time">${c.lastTime || ''}</span></div>
        <div class="chat-last">${last}</div>
      </div></div>`;
  }).join('') || '<div class="empty-state"><div class="es-icon">💬</div><div class="es-title">Чатов нет</div><div class="es-text">Нажмите ＋ чтобы начать новый чат.</div></div>';
  list.querySelectorAll('.chat-item').forEach(el => { el.onclick = () => openChat(el.dataset.id); });
}
document.getElementById('search-chats').addEventListener('input', e => renderChats(e.target.value));

/* ================= ЧАТ ================= */
function openChat(id) {
  currentChat = chats.find(c => c.id === id);
  if (!currentChat) return;
  document.getElementById('chat-title').textContent = currentChat.name;
  currentChat.messages = currentChat.messages || [];
  loadChatFromFirebase(id);
  document.getElementById('chat-screen').classList.add('active');
}
function loadChatFromFirebase(otherId) {
  const chatId = getChatId(myUid, otherId);
  db.ref('messages/' + chatId).off();
  db.ref('messages/' + chatId).on('child_added', snap => {
    const m = snap.val();
    if (currentChat && currentChat.messages.find(x => x.fireId === snap.key)) return;
    currentChat.messages.push({ from: m.from === myUid ? 'user' : 'bot', text: m.text, fireId: snap.key, author: m.from === myUid ? null : m.fromName });
    renderMessages();
    const c = chats.find(c => c.id === otherId);
    if (c) { c.messages = currentChat.messages; c.lastTime = new Date(m.time).toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'}); renderChats(); }
    if (localStorage.getItem('nexus_notify') !== 'off' && m.from !== myUid) toast('💬 ' + (m.fromName || 'Сообщение'));
  });
}
function renderMessages() {
  const box = document.getElementById('messages');
  if (!currentChat) return;
  box.innerHTML = currentChat.messages.map(m => {
    if (m.from === 'bot') return `<div class="msg bot">${m.author ? `<div class="msg-author">${m.author}</div>` : ''}${m.text}</div>`;
    return `<div class="msg user">${m.text}</div>`;
  }).join('');
  box.scrollTop = box.scrollHeight;
}
document.getElementById('btn-back-chat').onclick = () => {
  document.getElementById('chat-screen').classList.remove('active');
  if (currentChat) db.ref('messages/' + getChatId(myUid, currentChat.id)).off();
  currentChat = null; renderChats();
};
document.getElementById('btn-send').onclick = sendMessage;
document.getElementById('msg-input').addEventListener('keydown', e => { if (e.key === 'Enter') sendMessage(); });

function sendMessage() {
  const input = document.getElementById('msg-input');
  const text = input.value.trim();
  if (!text || !currentChat) return;
  input.value = '';
  currentChat.messages.push({ from: 'user', text });
  renderMessages();
  if (currentChat.isAI) { aiRespond(text); return; }
  const chatId = getChatId(myUid, currentChat.id);
  db.ref('messages/' + chatId).push({ from: myUid, fromName: user.name, text, time: Date.now() }).catch(err => toast('Ошибка: ' + err.message));
}

/* ================= AI ================= */
function aiRespond(text) {
  const box = document.getElementById('messages');
  const typing = document.createElement('div');
  typing.className = 'msg bot typing';
  typing.innerHTML = '<span class="dot-typing"></span><span class="dot-typing"></span><span class="dot-typing"></span>';
  box.appendChild(typing); box.scrollTop = box.scrollHeight;
  setTimeout(() => {
    typing.remove();
    const reply = aiReply(text);
    currentChat.messages.push({ from: 'bot', text: reply });
    renderMessages();
  }, 700);
}
function aiReply(text) {
  const t = text.toLowerCase().replace(/,/g, '.');
  const match = t.match(/(-?\d+(?:\.\d+)?)\s*([\+\-\*\/×÷])\s*(-?\d+(?:\.\d+)?)/);
  if (match) {
    const a = parseFloat(match[1]);
    const op = match[2];
    const b = parseFloat(match[3]);
    let res, opSym;
    if (op === '+') { res = a + b; opSym = '+'; }
    else if (op === '-') { res = a - b; opSym = '−'; }
    else if (op === '*' || op === '×') { res = a * b; opSym = '×'; }
    else if (op === '/' || op === '÷') {
      if (b === 0) return 'На ноль делить нельзя 😅';
      res = a / b; opSym = '÷';
    }
    return `${a} ${opSym} ${b} = ${res}`;
  }
  if (t.includes('привет')) return 'Привет! 👋 Напиши пример, например «2*3» или «10/2» — решу!';
  if (t.includes('как дела')) return 'Отлично! Готов решать примеры 😄';
  if (t.includes('спасибо')) return 'Пожалуйста! 🙌';
  if (t.includes('умнож')) return 'Умножение: напиши «a*b», например 7*8 = 56';
  if (t.includes('дел')) return 'Деление: напиши «a/b», например 10/2 = 5';
  return 'Я умею решать примеры на +, −, ×, ÷. Напиши, например: 12*4 или 100/5';
}

/* ================= ВХОДЯЩИЕ ================= */
function listenIncomingMessages() {
  if (!realChatsEnabled) return;
  db.ref('messages').on('child_added', chatSnap => {
    const chatId = chatSnap.key;
    if (!chatId.includes(myUid)) return;
    chatSnap.ref.on('child_added', msgSnap => {
      const m = msgSnap.val();
      if (m.from === myUid) return;
      const otherId = chatId.replace(myUid, '').replace('_', '').replace(/^_|_$/g, '');
      if (blockedUsers[otherId]) return;
      let chat = chats.find(c => c.id === otherId);
      if (!chat) {
        const sender = usersCache[otherId];
        chat = { id: otherId, name: sender ? sender.name : (m.fromName || 'Собеседник'), emoji: sender ? (sender.emoji || '👤') : '👤', messages: [], lastTime: '' };
        chats.push(chat);
      }
      if (!chat.messages.find(x => x.fireId === msgSnap.key)) {
        chat.messages.push({ from: 'bot', text: m.text, fireId: msgSnap.key, author: m.fromName });
        chat.lastTime = new Date(m.time).toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'});
        renderChats();
        if (currentChat && currentChat.id === chat.id) { currentChat.messages = chat.messages; renderMessages(); }
        else if (localStorage.getItem('nexus_notify') !== 'off') toast('💬 ' + (m.fromName || 'Новое сообщение'));
      }
    });
  });
}
function getChatId(a, b) { return [a, b].sort().join('_'); }

/* ================= НАСТРОЙКИ ================= */
document.getElementById('btn-settings-top').onclick = () => showScreen('screen-settings');
document.getElementById('nav-settings').onclick = () => showScreen('screen-settings');
document.getElementById('nav-main').onclick = () => { showScreen('screen-main'); renderChats(); };
document.getElementById('nav-chats').onclick = () => { showScreen('screen-main'); renderChats(); };
document.getElementById('btn-close-settings').onclick = () => showScreen('screen-main');

function openSub(id) {
  document.querySelectorAll('.subscreen').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  if (id === 'sub-admin') renderAdminUsers();
  if (id === 'sub-security') updateSecurityUI();
  if (id === 'sub-notify') {
    document.getElementById('toggle-notify').checked = localStorage.getItem('nexus_notify') !== 'off';
  }
  if (id === 'sub-account') {
    document.getElementById('acc-first-name').value = user.name.split(' ')[0] || '';
    document.getElementById('acc-last-name').value = user.name.split(' ').slice(1).join(' ') || '';
    renderBgGrid();
    renderProfileBanner();
  }
}
document.querySelectorAll('[data-close-sub]').forEach(b => {
  b.onclick = () => document.getElementById(b.dataset.closeSub).classList.remove('active');
});

document.querySelectorAll('.settings-row').forEach(row => {
  row.onclick = () => {
    const key = row.dataset.setting;
    if (key === 'account') openSub('sub-account');
    else if (key === 'notify') openSub('sub-notify');
    else if (key === 'security') openSub('sub-security');
    else if (key === 'admin') openSub('sub-admin');
    else {
      document.getElementById('generic-title').textContent = row.querySelector('.settings-title').textContent;
      openSub('sub-generic');
    }
  };
});

/* Аватар в настройках */
document.getElementById('settings-avatar-btn').onclick = () => document.getElementById('avatar-file-input').click();
document.getElementById('avatar-file-input').onchange = e => {
  const file = e.target.files[0]; if (!file) return;
  const reader = new FileReader();
  reader.onload = ev => {
    const img = document.getElementById('settings-avatar-img');
    img.src = ev.target.result; img.style.display = 'block';
    document.getElementById('settings-avatar-emoji').style.display = 'none';
    user.avatar = ev.target.result; toast('Фото обновлено');
  };
  reader.readAsDataURL(file);
};

/* ВИДЕО/ФОТО БАННЕР В НАСТРОЙКАХ */
const svVideo = document.getElementById('sv-video');
const svImg = document.getElementById('sv-img');
const svEmpty = document.getElementById('sv-empty');
document.getElementById('sv-edit').onclick = () => document.getElementById('sv-file').click();
document.getElementById('sv-file').onchange = e => {
  const file = e.target.files[0]; if (!file) return;
  const reader = new FileReader();
  reader.onload = ev => {
    const dataUrl = ev.target.result;
    if (file.type.startsWith('video/')) {
      svVideo.src = dataUrl; svVideo.style.display = 'block'; svImg.style.display = 'none';
      svEmpty.style.display = 'none'; user.banner = dataUrl; user.bannerType = 'video';
      document.getElementById('sv-clear').classList.add('show');
    } else {
      svImg.src = dataUrl; svImg.style.display = 'block'; svVideo.style.display = 'none';
      svEmpty.style.display = 'none'; user.banner = dataUrl; user.bannerType = 'image';
      document.getElementById('sv-clear').classList.add('show');
    }
    toast('Баннер обновлён');
  };
  reader.readAsDataURL(file);
};
document.getElementById('sv-clear').onclick = () => {
  svVideo.style.display = 'none'; svImg.style.display = 'none'; svEmpty.style.display = 'flex';
  svVideo.src = ''; svImg.src = '';
  user.banner = null; user.bannerType = null;
  document.getElementById('sv-clear').classList.remove('show');
};

/* ПРОФИЛЬ: БАННЕР */
const profBannerImg = document.getElementById('prof-banner-img');
const profBannerVideo = document.getElementById('prof-banner-video');
const profBannerEmpty = document.getElementById('prof-banner-empty');
document.getElementById('prof-banner-edit').onclick = () => document.getElementById('prof-banner-file').click();
document.getElementById('prof-banner-file').onchange = e => {
  const file = e.target.files[0]; if (!file) return;
  const reader = new FileReader();
  reader.onload = ev => {
    const dataUrl = ev.target.result;
        if (file.type.startsWith('video/')) {
      profBannerVideo.src = dataUrl; profBannerVideo.style.display = 'block'; profBannerImg.style.display = 'none';
      profBannerEmpty.style.display = 'none'; user.banner = dataUrl; user.bannerType = 'video';
    } else {
      profBannerImg.src = dataUrl; profBannerImg.style.display = 'block'; profBannerVideo.style.display = 'none';
      profBannerEmpty.style.display = 'none'; user.banner = dataUrl; user.bannerType = 'image';
    }
    document.getElementById('prof-banner-clear').classList.add('show');
    if (myUid) db.ref('users/' + myUid).update({ banner: user.banner, bannerType: user.bannerType });
    toast('Баннер профиля обновлён');
  };
  reader.readAsDataURL(file);
};
document.getElementById('prof-banner-clear').onclick = () => {
  profBannerImg.style.display = 'none'; profBannerVideo.style.display = 'none'; profBannerEmpty.style.display = 'flex';
  profBannerImg.src = ''; profBannerVideo.src = '';
  user.banner = null; user.bannerType = null;
  document.getElementById('prof-banner-clear').classList.remove('show');
  if (myUid) db.ref('users/' + myUid).update({ banner: null, bannerType: null });
};
function renderProfileBanner() {
  if (user.banner) {
    if (user.bannerType === 'video') {
      profBannerVideo.src = user.banner; profBannerVideo.style.display = 'block'; profBannerImg.style.display = 'none';
    } else {
      profBannerImg.src = user.banner; profBannerImg.style.display = 'block'; profBannerVideo.style.display = 'none';
    }
    profBannerEmpty.style.display = 'none';
    document.getElementById('prof-banner-clear').classList.add('show');
  } else {
    profBannerImg.style.display = 'none'; profBannerVideo.style.display = 'none'; profBannerEmpty.style.display = 'flex';
    document.getElementById('prof-banner-clear').classList.remove('show');
  }
}

/* ФОН ПРОФИЛЯ */
const BG_PRESETS = [
  'linear-gradient(135deg,#6c8cff,#b46cff)',
  'linear-gradient(135deg,#0ea5e9,#22c55e)',
  'linear-gradient(135deg,#f59e0b,#ef4444)',
  'linear-gradient(135deg,#8b5cf6,#ec4899)',
  'linear-gradient(135deg,#111827,#374151)',
  'linear-gradient(135deg,#f97316,#eab308)',
  'linear-gradient(135deg,#14b8a6,#0ea5e9)',
  'linear-gradient(135deg,#ec4899,#8b5cf6)',
  'linear-gradient(135deg,#22c55e,#84cc16)'
];
function renderBgGrid() {
  const grid = document.getElementById('bg-grid');
  grid.innerHTML = BG_PRESETS.map((bg) => `<div class="bg-option" data-bg="${bg}" style="background:${bg};"></div>`).join('') +
    (user.profileBg && !BG_PRESETS.includes(user.profileBg) ? `<div class="bg-option selected" data-bg="${user.profileBg}" style="background-image:url('${user.profileBg}');"></div>` : '');
  grid.querySelectorAll('.bg-option').forEach(el => {
    el.onclick = () => {
      user.profileBg = el.dataset.bg;
      grid.querySelectorAll('.bg-option').forEach(x => x.classList.remove('selected'));
      el.classList.add('selected');
      updateBgPreview();
    };
  });
  updateBgPreview();
}
function updateBgPreview() {
  const p = document.getElementById('profile-bg-preview');
  if (user.profileBg) {
    if (user.profileBg.startsWith('linear-gradient')) { p.style.background = user.profileBg; p.style.backgroundImage = 'none'; p.textContent = ''; }
    else { p.style.background = `url(${user.profileBg}) center/cover`; p.textContent = ''; }
  } else { p.style.background = '#1e1e1e'; p.style.backgroundImage = 'none'; p.textContent = 'Без фона'; }
}
document.getElementById('btn-upload-bg').onclick = () => document.getElementById('bg-file').click();
document.getElementById('bg-file').onchange = e => {
  const file = e.target.files[0]; if (!file) return;
  const reader = new FileReader();
  reader.onload = ev => { user.profileBg = ev.target.result; renderBgGrid(); };
  reader.readAsDataURL(file);
};
document.getElementById('btn-clear-bg').onclick = () => { user.profileBg = null; renderBgGrid(); };

/* АККАУНТ */
document.getElementById('account-avatar-btn').onclick = () => document.getElementById('account-avatar-file').click();
document.getElementById('account-avatar-file').onchange = e => {
  const file = e.target.files[0]; if (!file) return;
  const reader = new FileReader();
  reader.onload = ev => {
    const img = document.getElementById('account-avatar-img');
    img.src = ev.target.result; img.style.display = 'block';
    document.getElementById('account-avatar-emoji').style.display = 'none';
    user.avatar = ev.target.result;
  };
  reader.readAsDataURL(file);
};
document.getElementById('btn-save-account').onclick = () => {
  const first = document.getElementById('acc-first-name').value.trim();
  const last = document.getElementById('acc-last-name').value.trim();
  user.name = [first, last].filter(Boolean).join(' ') || 'Пользователь';
  document.getElementById('settings-name').textContent = user.name;
  if (myUid) db.ref('users/' + myUid).update({ name: user.name, profileBg: user.profileBg, avatar: user.avatar });
  const saved = getSavedAccount();
  if (saved) {
    saved.name = user.name; saved.avatar = user.avatar; saved.profileBg = user.profileBg;
    saveAccount(saved);
  }
  toast('Профиль сохранён');
  document.getElementById('sub-account').classList.remove('active');
};

/* УВЕДОМЛЕНИЯ */
document.getElementById('toggle-notify').onchange = e => {
  localStorage.setItem('nexus_notify', e.target.checked ? 'on' : 'off');
  toast(e.target.checked ? 'Уведомления включены' : 'Уведомления выключены');
};
document.getElementById('toggle-sound').onchange = e => {
  localStorage.setItem('nexus_sound', e.target.checked ? 'on' : 'off');
  toast('Звук ' + (e.target.checked ? 'вкл' : 'выкл'));
};
document.getElementById('toggle-vibrate').onchange = e => {
  localStorage.setItem('nexus_vibrate', e.target.checked ? 'on' : 'off');
  toast('Вибрация ' + (e.target.checked ? 'вкл' : 'выкл'));
};

/* БЕЗОПАСНОСТЬ */
function updateSecurityUI() {
  const has = hasPassword();
  document.getElementById('security-status').textContent = has ? 'Пароль установлен ✓' : 'Пароль не установлен';
  document.getElementById('btn-remove-password').style.display = has ? 'block' : 'none';
  document.getElementById('new-password').value = '';
  document.getElementById('confirm-password').value = '';
}
document.getElementById('btn-set-password').onclick = () => {
  const p1 = document.getElementById('new-password').value;
  const p2 = document.getElementById('confirm-password').value;
  if (!p1 || p1.length < 4) return toast('Пароль минимум 4 символа');
  if (p1 !== p2) return toast('Пароли не совпадают');
  localStorage.setItem('nexus_password', p1);
  toast('Пароль установлен');
  updateSecurityUI();
};
document.getElementById('btn-remove-password').onclick = () => {
  localStorage.removeItem('nexus_password');
  toast('Пароль удалён. Вход без пароля.');
  updateSecurityUI();
};

/* АДМИН-ПАНЕЛЬ */
let footerClicks = 0, footerTimer = null;
document.getElementById('version-footer').onclick = () => {
  footerClicks++;
  clearTimeout(footerTimer);
  footerTimer = setTimeout(() => { footerClicks = 0; }, 1500);
  if (footerClicks >= 7) {
    footerClicks = 0;
    document.getElementById('admin-pass-input').value = '';
    openSub('sub-admin-lock');
  }
};
document.getElementById('btn-admin-login').onclick = () => {
  const pass = document.getElementById('admin-pass-input').value;
  if (pass !== ADMIN_PASSWORD) return toast('Неверный пароль');
  toast('🔓 Доступ разрешён');
  openSub('sub-admin');
};

function renderAdminUsers() {
  const box = document.getElementById('admin-users-list');
  const ids = Object.keys(usersCache);
  if (!ids.length) { box.innerHTML = '<p class="sub">Пользователей нет</p>'; return; }
  box.innerHTML = ids.map(id => {
    const u = usersCache[id];
    const isBanned = blockedUsers[id] === 'banned' || u.banned;
    const isKicked = blockedUsers[id] === 'kicked';
    return `<div class="admin-user-card">
      <div class="admin-user-head">
        <div class="au-avatar">${u.emoji || '👤'}</div>
        <div class="au-info">
          <div class="au-name">
            ${u.name} ${id === myUid ? '<span class="badge badge-admin">вы</span>' : ''}
            ${isBanned ? '<span class="badge badge-banned">забанен</span>' : ''}
            ${isKicked ? '<span class="badge badge-kicked">кикнут</span>' : ''}
            ${u.online ? '<span class="badge badge-online">онлайн</span>' : ''}
          </div>
          <div class="au-phone">${u.phone || ('ID: ' + id.slice(0, 14))}</div>
        </div>
      </div>
      <div class="admin-actions">
        <button class="btn btn-sm btn-warn" data-act="kick" data-uid="${id}">👢 Кик</button>
        <button class="btn btn-sm btn-danger" data-act="ban" data-uid="${id}">🚫 Бан</button>
        <button class="btn btn-sm btn-outline" data-act="delete" data-uid="${id}">🗑 Удалить</button>
        <button class="btn btn-sm btn-outline" data-act="unban" data-uid="${id}">✅ Разбан</button>
      </div>
    </div>`;
  }).join('');
  box.querySelectorAll('[data-act]').forEach(btn => {
    btn.onclick = () => adminAction(btn.dataset.act, btn.dataset.uid);
  });
}
function adminAction(act, uid) {
  if (uid === myUid && (act === 'ban' || act === 'delete' || act === 'kick')) {
    return toast('Нельзя применить к себе');
  }
  if (act === 'kick') {
    blockedUsers[uid] = 'kicked';
    db.ref('users/' + uid).update({ kicked: true, online: false });
    toast('Пользователь кикнут');
  } else if (act === 'ban') {
    blockedUsers[uid] = 'banned';
    db.ref('users/' + uid).update({ banned: true, online: false });
    chats = chats.filter(c => c.id !== uid);
    toast('Пользователь забанен');
  } else if (act === 'delete') {
    delete blockedUsers[uid];
    db.ref('users/' + uid).remove();
    chats = chats.filter(c => c.id !== uid);
    toast('Пользователь удалён');
  } else if (act === 'unban') {
    delete blockedUsers[uid];
    db.ref('users/' + uid).update({ banned: false, kicked: false, online: true });
    toast('Пользователь разбанен');
  }
  renderAdminUsers();
  renderChats();
}

/* НОВЫЙ ЧАТ */
const newChatModal = document.getElementById('modal-new-chat');
const newChatSearch = document.getElementById('new-chat-search');
const newChatResults = document.getElementById('new-chat-results');
function openNewChatModal() {
  if (!realChatsEnabled) {
    toast('Сначала заполните имя и настоящий номер в профиле');
    showScreen('screen-profile');
    return;
  }
  newChatModal.classList.add('show');
  newChatSearch.value = '';
  renderNewChatResults('');
}
function closeNewChatModal() { newChatModal.classList.remove('show'); }
function renderNewChatResults(query) {
  const q = query.trim().toLowerCase();
  const realUsers = Object.keys(usersCache).filter(id => id !== myUid && !usersCache[id].banned).map(id => ({ id, ...usersCache[id] }));
  const filtered = realUsers.filter(u => u.name.toLowerCase().includes(q));
  let html = filtered.map(u => `<div class="chat-item" data-uid="${u.id}" style="padding:10px;">
      <div class="chat-avatar" style="width:44px;height:44px;font-size:22px;">${u.emoji || '👤'}</div>
      <div class="chat-info"><div class="chat-name">${u.name}</div><div class="chat-last">${u.phone || 'Нажмите, чтобы начать чат'}</div></div>
    </div>`).join('');
  if (!html) html = '<div style="color:#666;text-align:center;padding:20px;">Пользователей пока нет.</div>';
  html += `<div class="chat-item" data-uid="ai" style="padding:10px; border-top:1px solid #2a2a2a; margin-top:4px;">
      <div class="chat-avatar" style="width:44px;height:44px;font-size:22px;">🤖</div>
      <div class="chat-info"><div class="chat-name">Nexus AI (математика)</div><div class="chat-last">Решает примеры</div></div>
    </div>`;
  newChatResults.innerHTML = html;
  newChatResults.querySelectorAll('.chat-item').forEach(el => { el.onclick = () => startChatWith(el.dataset.uid); });
}
function startChatWith(uid) {
  let chat = chats.find(c => c.id === uid);
  if (!chat) {
    if (uid === 'ai') chat = { id: 'ai', name: 'Nexus AI', emoji: '🤖', isAI: true, messages: [{ from: 'bot', text: 'Привет! Напиши пример: 2*3 или 10/2' }], lastTime: 'сейчас' };
    else { const u = usersCache[uid] || { name: 'Собеседник', emoji: '👤' }; chat = { id: uid, name: u.name, emoji: u.emoji || '👤', messages: [], lastTime: '' }; }
    chats.unshift(chat);
  }
  closeNewChatModal(); renderChats(); openChat(chat.id);
}
document.getElementById('btn-new-chat').onclick = openNewChatModal;
document.getElementById('btn-cancel-new-chat').onclick = closeNewChatModal;
newChatSearch.addEventListener('input', e => renderNewChatResults(e.target.value));
document.getElementById('btn-create-ai-chat').onclick = () => startChatWith('ai');
newChatModal.addEventListener('click', e => { if (e.target === newChatModal) closeNewChatModal(); });

/* ================= СТАРТ ================= */
renderChats();
updateSavedHint();
document.getElementById('toggle-notify').checked = localStorage.getItem('nexus_notify') !== 'off';
document.getElementById('toggle-sound').checked = localStorage.getItem('nexus_sound') !== 'off';
document.getElementById('toggle-vibrate').checked = localStorage.getItem('nexus_vibrate') !== 'off';
</script>
</body>
</html>