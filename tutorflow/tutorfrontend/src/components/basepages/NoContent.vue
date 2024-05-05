<template>
    <div :class="type">
        <slot>{{ title }}</slot>
    </div>
</template>

<script>
export default {
    props: ['type', 'title']
};
</script>

<style scoped>
div{
    border: 1px solid rgb(114, 124, 138);
    padding: 20px;
    width: fit-content;
    border-radius: 5px;
}
.no-question{
    font-size: larger;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}
.page-not-found{
    margin: auto;
    font-weight: bold;
    font-size: larger;
    position: fixed;
    top:10%;
    left: 36%;
}

</style>