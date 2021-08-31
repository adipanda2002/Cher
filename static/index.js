function deleteReflection(reflectionId) {
    fetch("/delete-reflection", 
    {
      method: "POST",
      body: JSON.stringify({ reflectionId: reflectionId }),
    }).then((_res) => 
    {
      window.location.href = "/";
    });
    }