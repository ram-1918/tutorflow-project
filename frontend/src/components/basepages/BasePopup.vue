<template>
    <div :class="type">
        <slot>
            <span v-if="type==='loginerr'">
                <!-- {{ title }} -->
                Please 
                <router-link to="/register/">Register</router-link>
                or
                <router-link to="/login/">login</router-link>
                to add to Favorites!
            </span>
            <span v-else>
                {{ title }}
            </span>
        </slot>
    </div>
</template>

<script>
export default {
    props: ['type', 'title']
};
</script>

<style scoped>
div{
    padding: 10px;
    width: fit-content;
    border-radius: 10px;
    animation: fade 3s ease-in-out;
    left: 36%;
    position: absolute;
}
.feedback{
    background-color: rgb(5, 128, 7);
    color: white;
}
.loginerr{
    /* background-color: rgb(210, 224, 210); */
    background-color: rgb(197, 233, 197);
    color: rgb(42, 9, 9);
    animation: fade 8s ease-in-out;
}
.err{
    background-color: rgb(210, 224, 210);
    color: rgb(42, 9, 9);
    animation: fade 10s ease-in-out;
}
.add{
    background-color: rgb(9, 107, 11);
    color: white;
}
.delete{
    background-color: rgb(5, 67, 128);
    color: white;
}
.logout{
    background-color: rgb(128, 30, 5);
    color: white;
}
@keyframes fade{
    from {
        top: 10%;
        opacity: 1;
    }
    to {
        top: 0;
        opacity: 0;
    }
}
</style>