"""
farsi_widgets.py
-----------------
PersianTextInput: نسخه‌ای از TextInput که حین تایپ، حروف فارسی را
می‌چسباند (joining) و با base_direction='rtl' جهت و ترتیب درستی نشان
می‌دهد.

نکته‌ی مهم درباره‌ی طراحی: نسخه‌ی قبلی این فایل از یک ترفند «متن نامرئی
+ Label روکش» استفاده می‌کرد، ولی چون آن روش باعث می‌شد کلیک روی وسط
متن به موقعیت اشتباهی نگاشت شود (چون مختصات کلیک با متنِ واقعاً
نامرئی مطابقت نداشت)، ویرایش وسط جمله را خراب می‌کرد. برای همین به
نمایش مستقیمِ خودِ TextInput برگشتیم: همان چیزی که کاربر می‌بیند، همان
چیزی است که Kivy برای موقعیت مکان‌نما/کلیک استفاده می‌کند، پس ویرایش
همیشه در جای درست انجام می‌شود.
"""

from kivy.uix.textinput import TextInput

try:
    import arabic_reshaper
    _reshaper = arabic_reshaper.ArabicReshaper()
    _HAS_RESHAPER = True
except ImportError:
    _HAS_RESHAPER = False


class PersianTextInput(TextInput):
    def _create_line_label(self, text, hint=False):
        if _HAS_RESHAPER and text:
            try:
                text = _reshaper.reshape(text)
            except Exception:  # noqa: BLE001
                pass
        return super()._create_line_label(text, hint=hint)


# نگه‌داشتن نام قدیمی برای سازگاری با کدهایی که هنوز PersianInputBox
# را ایمپورت می‌کنند
PersianInputBox = PersianTextInput
