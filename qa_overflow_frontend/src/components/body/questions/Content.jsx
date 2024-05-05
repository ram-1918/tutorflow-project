import QContent from "./support/QContent.jsx";
import QFilters from "./support/QFilters.jsx";
import QHeader from "./support/QHeader.jsx";

export default function Content() {
    return (
        <div className="w-[85%] h-full border-l">
            <div className="w-full flex flex-col justify-start items-center border-b border-gray-200">
                <QHeader />
                <QFilters />
            </div>
            <QContent />
        </div>
    )
}