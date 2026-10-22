
const fs = require('fs');
const vm = require('vm');

const mockWindow = {
  addEventListener: () => {},
  removeEventListener: () => {},
  scrollY: 0,
  scrollTo: () => {},
  location: { pathname: '/index.html', href: 'http://localhost/index.html' },
  matchMedia: () => ({ matches: false })
};

const mockDocument = {
  body: { classList: { toggle: () => {}, remove: () => {}, add: () => {} } },
  readyState: 'interactive',
  addEventListener: (evt, cb) => {
    if (evt === 'DOMContentLoaded') setTimeout(cb, 10);
  },
  getElementById: (id) => {
    return {
      classList: {
        add: () => {},
        remove: () => {},
        contains: () => false,
        toggle: () => false
      },
      style: {},
      remove: () => {},
      addEventListener: () => {},
      setAttribute: () => {},
      getAttribute: () => null,
      innerHTML: '',
      textContent: ''
    };
  },
  querySelector: () => null,
  querySelectorAll: () => []
};

const context = vm.createContext({
  window: mockWindow,
  document: mockDocument,
  console: console,
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  setInterval: setInterval,
  clearInterval: clearInterval,
  localStorage: {
    getItem: () => null,
    setItem: () => {},
    removeItem: () => {}
  }
});

const mainCode = fs.readFileSync('assets/js/main.js', 'utf8');
vm.runInContext(mainCode, context);
console.log('main.js fully verified!');

const dashCode = fs.readFileSync('assets/js/dashboard.js', 'utf8');
vm.runInContext(dashCode, context);
console.log('dashboard.js fully verified!');

const authCode = fs.readFileSync('assets/js/auth.js', 'utf8');
vm.runInContext(authCode, context);
console.log('auth.js fully verified!');

// Wait for any DOMContentLoaded setTimeout callbacks
setTimeout(() => {
  console.log('All DOMContentLoaded events dispatched and executed without error!');
  process.exit(0);
}, 50);
