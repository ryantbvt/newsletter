import { CreatePostDto, PostResponse } from '../types/post';
import apiConfig from '../../../config/api.config';

// Build endpoint path using the base URL and endpoint-specific version and path
const POSTS_ENDPOINT = `${apiConfig.baseUrl}${apiConfig.endpoints.posts.version}${apiConfig.endpoints.posts.path}`;

/**
 * Post API service with methods to interact with the post endpoints
 */
export const postService = {
  /**
   * Creates a new post on the server
   * 
   * @param {CreatePostDto} postData - The post data containing title and content
   * @returns {Promise<PostResponse>} A promise that resolves to the created post with ID and other server-added fields
   * @throws {Error} Throws an error if the API request fails with the error message from the server
   * 
   * @example
   * // Example usage:
   * const newPost = await postService.createPost({
   *   title: "My awesome post",
   *   content: "This is the content of my post"
   * });
   * console.log(newPost.id); // The ID of the newly created post
   */
  async createPost(postData: CreatePostDto): Promise<PostResponse> {
    const response = await fetch(`${POSTS_ENDPOINT}/create`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(postData),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Failed to create post');
    }

    return response.json();
  },
  
  /**
   * Fetches all posts from the server
   * 
   * @returns {Promise<PostResponse[]>} A promise that resolves to an array of posts
   * @throws {Error} Throws an error if the API request fails
   */
  async getPosts(): Promise<PostResponse[]> {
    const response = await fetch(`${POSTS_ENDPOINT}/`);
    
    if (!response.ok) {
      throw new Error('Failed to fetch posts');
    }
    
    return response.json();
  },
  
  /**
   * Fetches a single post by its ID
   * 
   * @param {number} id - The ID of the post to fetch
   * @returns {Promise<PostResponse>} A promise that resolves to the post
   * @throws {Error} Throws an error if the API request fails or post is not found
   */
  async getPostById(id: number): Promise<PostResponse> {
    const response = await fetch(`${POSTS_ENDPOINT}/${id}`);
    
    if (!response.ok) {
      throw new Error(`Failed to fetch post with ID ${id}`);
    }
    
    return response.json();
  }
}; 