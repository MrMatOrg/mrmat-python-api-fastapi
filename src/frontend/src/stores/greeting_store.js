import { defineStore } from 'pinia'

export const useGreetingStore = defineStore({
  id: 'greeting',
  state: () => ({
    greeting_v1: '',
    counter: 0
  }),
  getters: {
    doubleCount: (state) => state.counter * 2
  },
  actions: {
    increment() {
      this.counter++
    },
    greet_v1() {
      fetch('/api/greeting/v1')
          .then(response => response.json)
          .then(data => this.greeting_v1 = data.message)
    }
  }
})
