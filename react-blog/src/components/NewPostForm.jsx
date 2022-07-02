import React, {useState, useEffect} from "react";

const PostForm = function() {
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
        <div className="post-form">
            <input className="title-input" type="text" />
            <input className="text-input" type="text" />
            <button className="submit-btn" type="submit">submit</button>
        </div>
    );   
}

export default Post;