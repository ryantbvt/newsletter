import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import { postService } from "../posts/shared/api/postService";
import { PostResponse } from "../posts/shared/types/post";

export default function SinglePostPage() {
  const { id } = useParams<{ id: string }>();
  const [post, setPost] = useState<PostResponse | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchPost = async () => {
      if (!id) {
        setError("No post ID provided");
        setIsLoading(false);
        return;
      }

      console.log("Fetching post with ID:", id, typeof id);
      
      // Ensure id is a valid number
      const postId = Number(id);
      if (isNaN(postId)) {
        setError(`Invalid post ID: ${id}`);
        setIsLoading(false);
        return;
      }
      
      try {
        const postData = await postService.getPostById(postId);
        console.log("Fetched post data:", postData);
        setPost(postData);
      } catch (err) {
        console.error("Error fetching post:", err);
        setError("Failed to load post. It may not exist or has been removed.");
      } finally {
        setIsLoading(false);
      }
    };

    fetchPost();
  }, [id]);

  if (isLoading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-emerald-500"></div>
      </div>
    );
  }

  if (error || !post) {
    return (
      <div className="max-w-3xl mx-auto py-10 px-4 text-center">
        <div className="bg-white p-8 rounded-lg shadow-md">
          <p className="text-xl text-red-500 mb-6">{error || "Post not found"}</p>
          <Link 
            to="/newsletters" 
            className="inline-block px-6 py-2 bg-emerald-500 text-white rounded-lg hover:bg-emerald-600"
          >
            Back to Newsletters
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto py-10 px-4">
      <div className="bg-white p-8 rounded-lg shadow-md">
        <h1 className="text-3xl font-bold text-gray-800 mb-6">{post.title}</h1>
        <div className="prose max-w-none">
          <p className="text-gray-700 whitespace-pre-wrap">{post.content}</p>
        </div>
        
        <div className="mt-10 pt-6 border-t border-gray-200">
          <Link 
            to="/newsletters" 
            className="inline-flex items-center text-emerald-600 hover:text-emerald-700"
          >
            &larr; Back to all newsletters
          </Link>
        </div>
      </div>
    </div>
  );
} 