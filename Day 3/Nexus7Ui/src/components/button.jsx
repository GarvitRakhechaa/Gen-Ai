// src/components/button.jsx

import { Button as ShadcnButton } from "./ui/button";
import { useEffect, useRef } from 'react';
import gsap from 'gsap';

function Button(props) {
  const buttonRef = useRef(null);

  useEffect(() => {
    const el = buttonRef.current;

    gsap.set(el, { scale: 1, opacity: 1, rotate: 0, clearProps: "backgroundColor" });

    if (props.disabled) {
      gsap.to(el, {
        duration: 0.3,
        opacity: 0.5,
        scale: 0.9,
        backgroundColor: "#9CA3AF", // Gray-400
        rotate: 0,
        overwrite: "auto",
        cursor: 'not-allowed'
      });
    } else {
      el.addEventListener("mouseenter", () => {
        gsap.to(el, {
          duration: 0.3,
          scale: props.hoverScale || 1.1,
          backgroundColor: props.hoverColor || "#6366F1", // Default Indigo-500
          rotate: props.hoverRotate || 0,
          overwrite: "auto"
        });
      });

      el.addEventListener("mouseleave", () => {
        gsap.to(el, {
          duration: 0.3,
          scale: 1,
          backgroundColor: props.backgroundColor || null, // Remove background color
          rotate: 0,
          overwrite: "auto"
        });
      });
    }

    return () => {
      el.removeEventListener("mouseenter", () => {});
      el.removeEventListener("mouseleave", () => {});
    };

  }, [props.hoverColor, props.backgroundColor, props.hoverRotate, props.hoverScale, props.disabled]);

  return (
    <ShadcnButton
      {...props}
      ref={buttonRef}
      style={{ cursor: props.disabled ? 'not-allowed' : 'pointer' }}
      disabled={props.disabled}
    > 
      {props.children}
    </ShadcnButton>
  );
}

export default Button;