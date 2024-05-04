import AuthButtons from "./AuthButtons";
import SearchBar from "./SearchBar";
import Title from "./Title";

const Topnav = () => {
    return (
        <header 
        className="px-[10%] py-2 border-b-2 border-blue-300 flex flex-row justify-between items-center space-x-10">
            <div className="bg-red-300">
                <Title />
            </div>
            <div className="flex flex-row items-center justify-between space-x-10">
                <SearchBar />
                <AuthButtons />
            </div>
        </header>
    );
};

export default Topnav;