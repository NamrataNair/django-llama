<template>
  <div class="w-full flex justify-center p-5">
    <div class="flex flex-col max-w-[45rem]">
      <div class="text-xl"> Commercial Email Writer</div>
      <div class="mt-5">
        <span class="p-float-label">
          <InputText id="theme" type="text" v-model="theme" />
          <label for="username">Theme</label>
        </span>
      </div>
      <div>
        <div class="mt-3">
          Makrketing Director
          {{ theme }} sur la base de ces informations:
        </div>
      </div>
      <div class="flex flex-col max-w-[45rem]">
        <div class="pt-8">
          <span class="p-float-label">
            <Textarea id="prompt" v-model="prompt" rows="5" class="w-full" autoResize />
            <label for="prompt">Prompt</label>
          </span>
        </div>
        <div class="pt-5 text-center">
          <button class="w-full btn secondary" @click="infer()" v-if="!lmState.isStreaming == true"
            :disabled="lmState.isRunning == true || prompt.length == 0">Envoyer</button>
        </div>
        <div v-if="lmState.isRunning == true && lmState.isStreaming == false">
          <LoadingSpinner class="pt-16 text-6xl txt-lighter" />
        </div>
        <div v-if="lmState.isStreaming == true">
          <button class="btn danger" @click="abort()">Stop</button>
        </div>
        <div class="mt-8 text-justify">
          <div v-html="stream.replaceAll('\n', '<br />').replaceAll('\t', '&nbsp;&nbsp;')"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onBeforeMount, reactive, nextTick } from 'vue';
import Textarea from 'primevue/textarea';
import { api } from '@/state';
import LoadingSpinner from '@/widgets/LoadingSpinner.vue';
import InputText from 'primevue/inputtext';

const template = `<s>[INST] <<SYS>>
Vous êtes Vigogne, un assistant IA créé par Zaion Lab. Vous suivez extrêmement bien les instructions. Aidez autant que vous le pouvez.
<</SYS>>

Marketing Director:

{prompt} [/INST]`;
const prompt = ref(``);
const theme = ref("ML Ops");
const result = ref("");
const stream = ref("");
const lmState = reactive({
  isRunning: false,
  isStreaming: false,
})

let i = 0;
const onChunk = (payload: Record<string, any>) => {
  console.log(">>", payload);
  nextTick(() => {
    window.scrollTo({
      top: document.body.scrollHeight,
      behavior: 'smooth'
    });
  });
  if (i == 0) {
    lmState.isStreaming = true
  }
  if (payload["num"] == 1) {
    lmState.isStreaming = true;
  }
  stream.value += payload
  ++i
};
const abortController = new AbortController();

async function infer() {
  stream.value = "";
  lmState.isRunning = true;
  let tpl = template.replace("{theme}", theme.value);
  tpl = tpl.replace("{prompt}", prompt.value);
  await api.postSse<Record<string, any>>(
    "/llm/generate/",
    { prompt: tpl, params: { temperature: 0.2, max_tokens: -1 } },
    onChunk,
    abortController,
    false,
    false,
    true,
    false,
  )
  lmState.isStreaming = false;
  lmState.isRunning = false;
}

function abort() {
  abortController.abort();
  lmState.isStreaming = false;
  lmState.isRunning = false;
}

onBeforeMount(() => result.value = "")
</script>