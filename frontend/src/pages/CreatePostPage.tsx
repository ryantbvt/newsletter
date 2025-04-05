import AddPostForm from "../posts/editor/components/AddPostForm";

export default function CreatePostPage() {
  const handleAddPost = (title: string, content: string) => {
    console.log('New post:', { title, content });
    // Here you would typically save the post to your backend
  };

  return (
    <main className="py-10 h-screen space-y-8 overflow-y-auto container mx-auto px-4">
      <h1 className="text-center font-bold text-3xl text-gray-800 tracking-wide">
        Create Post
      </h1>
      <div className="max-w-xl mx-auto bg-white rounded-xl p-8 shadow-lg">
        <AddPostForm
          onSubmit={handleAddPost}
        />
      </div>
    </main>
  );
} 