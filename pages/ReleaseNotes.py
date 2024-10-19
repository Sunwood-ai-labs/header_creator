import streamlit as st
import os
import glob

# リリースノートの表示
st.title("📝 リリースノート")
release_notes_files = glob.glob("docs/*.md")
if release_notes_files:
    for file_path in release_notes_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                release_content = f.read()
            st.markdown(f"### {os.path.basename(file_path)}")
            st.markdown(release_content, unsafe_allow_html=True)
            st.markdown("---")
        except Exception as e:
            st.error(f"{file_path}の読み込み中にエラーが発生しました: {e}")
else:
    st.error("リリースノートのMarkdownファイルが見つかりませんでした。")
