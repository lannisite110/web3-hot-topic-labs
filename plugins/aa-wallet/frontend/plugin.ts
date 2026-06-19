export const plugin = {
  id: 'edu.hot.aa-wallet',
  title: 'Account Abstraction Wallet Lab',
  routePrefix: '/labs/edu.hot.aa-wallet',
  routes: [{ path: '', component: () => import('./HotLab.vue') }],
  apiBase: '/api/v1/labs/edu.hot.aa-wallet',
}

export default plugin
