<script setup>
    import Button from './Button.vue'
</script>

<template>
    <div class="p-5 flex flex-col">
        <h3 class="text-center">Is this image okay?</h3>
        <div class="flex justify-center">
            <img src="../assets/logo.svg" width="75" />
        </div>
        <div class="flex flex-row gap-2 justify-center m-2">
            <Button txt="Use a different image" />
            <Button txt="Yes, banyaynay-ify" />
        </div>
        
    </div>
</template>