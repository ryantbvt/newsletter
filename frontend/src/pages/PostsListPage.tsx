import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { postService } from "../posts/shared/api/postService";
import { PostResponse } from "../posts/shared/types/post";

export default function PostsListPage() {
  const [posts, setPosts] = useState<PostResponse[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const postsData = await postService.getPosts();
        console.log("Posts data (raw):", JSON.stringify(postsData));
        
        // Check if posts have IDs and add them if they don't
        const postsWithIds = postsData.map((post, index) => {
          if (post.id === undefined) {
            console.log(`Post at index ${index} missing ID, adding ID=${index + 1}`);
            return { ...post, id: index + 1 };
          }
          return post;
        });
        
        console.log("Posts data (with IDs):", postsWithIds);
        setPosts(postsWithIds);
      } catch (err) {
        setError("Failed to load posts. Please try again later.");
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchPosts();
  }, []);

  if (isLoading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-emerald-500"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex justify-center items-center h-screen">
        <div className="text-red-500 text-center">
          <p className="text-xl">{error}</p>
          <button 
            onClick={() => window.location.reload()} 
            className="mt-4 px-4 py-2 bg-emerald-500 text-white rounded hover:bg-emerald-600"
          >
            Try Again
          </button>
        </div>
      </div>
    );
  }

  console.log("Rendering posts:", posts);

  return (
    <div className="max-w-4xl mx-auto py-10 px-4">
      <h1 className="text-3xl font-bold text-gray-800 mb-8">All Posts</h1>
      
      {posts.length === 0 ? (
        <div className="text-center py-10">
          <p className="text-xl text-gray-600">No posts found.</p>
          <Link 
            to="/create-post" 
            className="inline-block mt-4 px-6 py-2 bg-emerald-500 text-white rounded-lg hover:bg-emerald-600"
          >
            Create Your First Post
          </Link>
        </div>
      ) : (
        <div className="grid gap-6">
          {posts.map((post) => {
            console.log("Rendering post:", post.id, post);
            return (
              <div key={post.id} className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
                <Link to={`/newsletter/${post.id}`} className="block">
                  <h2 className="text-xl font-semibold text-emerald-700 hover:text-emerald-500 transition-colors">
                    {post.title}
                  </h2>
                </Link>
              </div>
            );
          })}
        </div>
      )}
      
      <div className="mt-8 text-center">
        <Link 
          to="/create-post" 
          className="inline-flex items-center px-6 py-3 rounded-full bg-emerald-500 text-white font-medium hover:bg-emerald-600 transition-all shadow-lg hover:shadow-xl"
        >
          Create New Post
        </Link>
      </div>
    </div>
  );
}