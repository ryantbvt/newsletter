export interface Post {
    id: number;
    title: string;
    content: string;
    published: boolean;
}

export interface CreatePostDto {
    title: string;
    content: string;
}

export type PostResponse = Post

// export interface PostResponse extends Post {
//   // Any additional fields from server response
// }

export interface FormStatus {
    message: string;
    isError: boolean;
  }