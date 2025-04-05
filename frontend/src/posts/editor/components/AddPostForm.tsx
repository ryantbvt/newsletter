import { usePost } from "../hooks/usePost";

export default function AddPostForm() {
    const { formData, handleChange, handleSubmit, isSubmitting, status } = usePost();

    return(
        <form 
        className="flex flex-col gap-6 w-full" 
        onSubmit={handleSubmit}
        >
            {status.message && (
                <div className={`p-3 rounded-lg ${status.isError ? 'bg-red-100 text-red-700' : 'bg-green-100 text-green-700'}`}>
                    {status.message}
                </div>
            )}
            
            <div className="space-y-2">
                <label htmlFor="title" className="text-gray-700 font-medium block">
                    Title
                </label>
                <input 
                    id="title"
                    name="title"
                    value={formData.title}
                    onChange={handleChange}
                    placeholder="Enter your post title"
                    className="rounded-lg w-full p-3 bg-gray-50 shadow-inner border border-gray-200 focus:ring-2 focus:ring-emerald-400 focus:outline-none"
                />
            </div>
            <div className="space-y-2">
                <label htmlFor="content" className="text-gray-700 font-medium block">
                    Content
                </label>
                <textarea 
                    id="content"
                    name="content"
                    value={formData.content}
                    onChange={handleChange}
                    placeholder="Share your thoughts..."
                    rows={6}
                    className="rounded-lg w-full p-3 bg-gray-50 shadow-inner border border-gray-200 focus:ring-2 focus:ring-emerald-400 focus:outline-none"
                />
            </div>
            <button
                type="submit"
                disabled={isSubmitting}
                className="self-end px-6 py-2.5 rounded-lg bg-emerald-500 text-white font-medium hover:bg-emerald-600 transition-all shadow-md disabled:opacity-50 disabled:cursor-not-allowed"
            >
                {isSubmitting ? 'Posting...' : 'Post'}
            </button>
        </form>
    )
}