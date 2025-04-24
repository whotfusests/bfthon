        function copyInstall() {
            const text = "pip install git+https://github.com/whotfusests/bfthon.git";
            navigator.clipboard.writeText(text).then(() => {
                const btn = document.querySelector('.btn-primary');
                btn.textContent = "Copied!";
                setTimeout(() => {
                    btn.textContent = "Install";
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy.', err);
            });
        }