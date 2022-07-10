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
 <p>Home</p>
  <p v-if="loggedIn">You are logged in</p>
  <p v-else>You are not logged in</p>
</template>

<script>
import { useAuthStore} from "@/stores/auth";

export default {
  name: "HomeComponent",
  // setup() {
  //   const authStore = useAuthStore()
  //   return { authStore }
  // },
  mounted() {
    console.log('Log in state: ' + this.loggedIn)
  },
  computed: {
    loggedIn() { return this.authStore.loggedIn }
  }
}
</script>

<style scoped>

</style>
