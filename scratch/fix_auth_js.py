with open('assets/js/auth.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = '''    // Role validation
    const selectedRole = roleSelect ? roleSelect.value : 'Chief Information Security Officer (CISO)';

    if (!isValid) {
      if (firstInvalidField) firstInvalidField.focus();
      return;
    }

    // Successful login simulation (Accepts any valid formatted credentials or matching demo user)
    const users = auth.getUsers();
    let matchedUser = users.find(u => u.email.toLowerCase() === emailVal.toLowerCase());

    if (!matchedUser) {
      // Create user profile for arbitrary valid credentials
      matchedUser = {
        firstName: emailVal.split('@')[0],
        lastName: 'Officer',
        email: emailVal,
        role: selectedRole
      };
    } else {
      matchedUser.role = selectedRole; // Update with selected role
    }

    auth.login(matchedUser, selectedRole);'''

replacement = '''    // Role validation (Strict: require user to select one)
    const selectedRole = roleSelect ? roleSelect.value : '';
    const roleError = document.getElementById('signin-role-error');
    if (!selectedRole) {
      isValid = false;
      if (roleSelect) roleSelect.classList.add('has-error');
      if (roleError) roleError.style.display = 'block';
      if (!firstInvalidField) firstInvalidField = roleSelect;
    } else {
      if (roleSelect) roleSelect.classList.remove('has-error');
      if (roleError) roleError.style.display = 'none';
    }

    if (!isValid) {
      if (firstInvalidField) firstInvalidField.focus();
      return;
    }

    // Successful login: Name is derived directly from user login credentials
    const users = auth.getUsers();
    let matchedUser = users.find(u => u.email.toLowerCase() === emailVal.toLowerCase());

    if (!matchedUser) {
      // Format username nicely from email: e.g. "john.doe" -> "John Doe"
      const rawUserPart = emailVal.split('@')[0];
      const cleanName = rawUserPart.split(/[._-]/).map(part => part.charAt(0).toUpperCase() + part.slice(1).toLowerCase()).join(' ') || 'Security Commander';
      
      matchedUser = {
        firstName: cleanName.split(' ')[0] || cleanName,
        lastName: cleanName.split(' ').slice(1).join(' ') || 'Officer',
        name: cleanName,
        email: emailVal,
        role: selectedRole
      };
    } else {
      matchedUser.role = selectedRole;
      if (!matchedUser.name) {
        matchedUser.name = `${matchedUser.firstName || ''} ${matchedUser.lastName || ''}`.trim() || matchedUser.username || emailVal.split('@')[0];
      }
    }

    auth.login(matchedUser, selectedRole);'''

js_norm = js.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
if target_norm in js_norm:
    js = js_norm.replace(target_norm, replacement)
    with open('assets/js/auth.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("auth.js updated with strict role validation and dynamic credential name!")
else:
    print("Could not match target in auth.js")

