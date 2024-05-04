export default function BaseButton({content, bg, border, text, width}) {
    // Dynamic Styling overrides the style defined in the classname
    const dynamicStyle = {
        backgroundColor:bg, 
        borderColor:border, 
        color:text, 
        width:width
    };
    return (
        <button 
        style={dynamicStyle}
        className="w-20 p-2 border rounded-lg hover:opacity-70"
        >{content}</button>
    )
}