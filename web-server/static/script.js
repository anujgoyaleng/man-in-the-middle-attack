const loginSection = document.getElementById('login-section');
const dashboardSection = document.getElementById('dashboard-section');
const messageDiv = document.getElementById('message');

document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password })
        });
        
        const data = await response.json();
        
        if (data.success) {
            showMessage('Login successful!', 'success');
            loginSection.style.display = 'none';
            dashboardSection.style.display = 'block';
            updateUserInfo(data);
        } else {
            showMessage(data.message, 'error');
        }
    } catch (error) {
        showMessage('Connection error', 'error');
    }
});

document.getElementById('transfer-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const amount = document.getElementById('amount').value;
    const toAccount = document.getElementById('to-account').value;
    
    try {
        const response = await fetch('/transfer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ amount, to_account: toAccount })
        });
        
        const data = await response.json();
        
        if (data.success) {
            showMessage(data.message, 'success');
            document.getElementById('user-info').innerHTML = `
                <p><strong>Balance:</strong> $${data.new_balance}</p>
            `;
        } else {
            showMessage(data.message, 'error');
        }
    } catch (error) {
        showMessage('Transfer failed', 'error');
    }
});

document.getElementById('logout-btn').addEventListener('click', () => {
    loginSection.style.display = 'block';
    dashboardSection.style.display = 'none';
    document.getElementById('login-form').reset();
    showMessage('Logged out', 'success');
});

function updateUserInfo(data) {
    document.getElementById('user-info').innerHTML = `
        <p><strong>Welcome:</strong> ${data.user}</p>
        <p><strong>Account:</strong> ${data.account}</p>
        <p><strong>Balance:</strong> $${data.balance}</p>
    `;
}

function showMessage(msg, type) {
    messageDiv.textContent = msg;
    messageDiv.className = `message ${type}`;
    setTimeout(() => {
        messageDiv.textContent = '';
        messageDiv.className = 'message';
    }, 3000);
}
