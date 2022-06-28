import React, {useState, useEffect} from "react";

const Post = function() {
    const [post, setPost] = useState([{}])

    useEffect(()=> {
        fetch("/blog/").then(
            res => res.json()
        ).then(
            data => {
                setPost(data)
                console.log(data)
            }
        )
    }, [])

    return(
        <div className="post">
            <h1>{post.title}</h1>
            <span>{post.text}</span>
            <span>{post.pub_date}</span>
        </div>
    );   
}

export default Post;