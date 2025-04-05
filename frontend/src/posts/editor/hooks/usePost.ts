import { useState, ChangeEvent, FormEvent } from "react";
import { CreatePostDto, FormStatus } from "../../shared/types/post";
import { postService } from "../../shared/api/postService";

export const usePost = () => {
    const[formData, setFormData] = useState<CreatePostDto>({
        title: '',
        content: ''
    });

    const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
    const [status, setStatus] = useState<FormStatus>({
        message: '',
        isError: false
    });

    const handleChange = (e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setIsSubmitting(true);
        setStatus({message: '', isError: false});

        try {
            await postService.createPost(formData);
            setStatus({
                message: 'Post created successfully!',
                isError: false
            });
            // Reset form after successful submission
            setFormData({ title: '', content: '' });
        } catch (error) {
            setStatus({
                message: error instanceof Error ? error.message : 'Failed to create post',
                isError: true
            });
        } finally {
            setIsSubmitting(false);
        }
    };

    return {
        formData,
        handleChange,
        handleSubmit,
        isSubmitting,
        status
    };
};