<!--
  - MIT License
  -
  - Copyright (c) 2022 Mathieu Imfeld
  -
  - Permission is hereby granted, free of charge, to any person obtaining a copy
  - of this software and associated documentation files (the "Software"), to deal
  - in the Software without restriction, including without limitation the rights
  - to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  - copies of the Software, and to permit persons to whom the Software is
  - furnished to do so, subject to the following conditions:
  -
  - The above copyright notice and this permission notice shall be included in
  - all copies or substantial portions of the Software.
  -
  - THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  - IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  - FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  - AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  - LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  - OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  - SOFTWARE.
  -->

<template>
  <sui-form class="attached fluid segment">
    <sui-header dividing>Greeting v1</sui-header>
    <sui-form-field>
      <sui-message visible>{{ state.message }}</sui-message>
    </sui-form-field>
    <sui-button primary @click="get_greeting">Get a greeting</sui-button>
  </sui-form>
  <sui-message attached="bottom" negative header="An error has occurred" v-if="errorVisible">
    {{ state.error }}
  </sui-message>
</template>

<script setup>
import { reactive, computed } from 'vue'

const state = reactive({
  error: '',
  message: 'Click the button to get a message from the Greeting V1 API'
})

const errorVisible = computed(() => {
  return state.error !== ''
})

function get_greeting(event) {
  fetch('/api/greeting/v1', { cache: "no-cache" })
      .then(response => {
        if(! response.ok) { throw new Error('Request has failed')}
        return response.json()
      })
      .then(json => { state.message = json.message })
      .catch(error => { state.error = error.message })
  if(event) event.preventDefault()
}

</script>

<style scoped>
.ui.visible.message {
  width: 80%;
  margin-right: 21px;
}
</style>
