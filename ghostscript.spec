#
# Conditional build:
# bcond_on_svgalib
#
Summary:	PostScript & PDF interpreter and renderer
Summary(de):	PostScript & PDF Interpreter und Renderer
Summary(fr):	Interpréteur et visualisateur PostScript & PDF
Summary(ja):	PostScript ¥¤¥ó¥¿¡¼¥×¥ê¥¿¡¦¥ì¥ó¥À¥é¡¼
Summary(pl):	Bezp³atny interpreter PostScriptu & PDF
Summary(tr):	PostScript & PDF yorumlayýcý ve gösterici
Name:		ghostscript
Version:	6.50
Release:	2
Vendor:		Aladdin Enterprises <bug-gs@aladdin.com>
Copyright:	Aladdin Free Public License
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source0:	ftp://download.sourceforge.net/pub/sourceforge/ghostscript/%{name}-%{version}.tar.bz2
Source1:	http://www.ozemail.com.au/~geoffk/pdfencrypt/pdf_sec.ps
# we need to link with libjpeg recompiled with our parameters
Source2:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v6b.tar.gz
Source3:	%{name}-find_devs.sh
Patch0:		%{name}-config.patch
Patch1:		%{name}-hpdj_driver.patch
Patch2:		%{name}-cdj880.patch
URL:		http://www.ghostscript.com/
# Required by ghostscript-find_devs.sh
BuildRequires:	awk
BuildRequires:	XFree86-devel
# Required by 'gdevvglb' device.
%ifnarch sparc sparc64 alpha
%{?bcond_on_svgalib:BuildRequires:	svgalib-devel}
%endif
BuildRequires:	zlib-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ghostscript is a PostScript interpretor. It can render both PostScript
and PDF compliant files to devices which include an X window, many
printer formats (including support for color printers), and popular
graphics file formats.

%description -l de
Ghostscipt ist ein PostScript-Interpretierer. Er kann sowohl
PostScript als auch PDF-konforme Dateien an Geräte ausgeben, zu denen
ein X-Fenster, viele Druckerformate (einschließlich Support für
Farbdrucker) und gängige Grafikdateiformate zählen.

%description -l fr
Ghostscript est un interpréteur PostScript. Il peut rendre des
fichiers PostScript ou PDF sur des périphériques dont une fenêtre X,de
nombreux types d'imprimantes (dont un support pour imprimantes
couleur), et des formats de fichiers graphiques populaires.

%description -l ja
Ghostscript ¤Ï PostScript ¥¤¥ó¥¿¡¼¥×¥ê¥¿¤Ç¤¹¡£¥Ý¥¹¥È¥¹¥¯¥ê¥×¥È¤È PDF
¤ò¥ì¥ó¥À¥ê¥ó¥°¤·¡¢X window ¤äÂ¾¤Î¥×¥ê¥ó¥¿¥Õ¥©¡¼¥Þ¥Ã¥È¤Ç½ÐÎÏ
¤·¤Þ¤¹¡£¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤ÏÆüËÜ¸ìÂÐ±þ¤·¤Æ¤¤¤Þ¤¹¡£

%description -l pl
Ghostcript jest interpreterem PostScriptu, jêzyku u¿ywanego do opisu
formatu dokumentu. Ghostscript potrafi przetworzyæ dokument w formacie
PostScript i PDF na szereg postaci wyj¶ciowych: drukarki (w³±czaj±c
kolorowe), okno X-Window i popularne formaty graficzne.

%description -l tr
GhostScript, PostScript ve PDF uyumlu dosyalarý, X penceresinde
gösterebilir ve birçok yazýcýnýn (renkli yazýcýlar dahil) basabileceði
biçime getirebilir.

%prep
%setup -q -n gs%{version}
ln -s src/unix-gcc.mak Makefile
%patch0 -p1
%patch1 -p1
%patch2 -p1
%setup -q -T -D -a 2 -n gs%{version}
ln -s jp* jpeg
install %{SOURCE3} .

%build
%{__make} \
	XCFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS} -DA4=1 -w" \
	XLDFLAGS="-s" \
	prefix=%{_prefix} \
	datadir=%{_datadir}/%{name} \
	mandir=%{_mandir} \
	docdir=%{_datadir}/doc/%{name}-%{version} \
	DEVICE_DEVS16="`/bin/sh %{SOURCE3} devs.mak \
%ifarch sparc sparc64 alpha
		vgalib \
%else
		%{!?bcond_on_svgalib:vgalib} \
%endif
		`" \
	DEVICE_DEVS17="`/bin/sh %{SOURCE3} contrib.mak \
%ifarch sparc sparc64 alpha
		vgalib \
%else
		%{!?bcond_on_svgalib:vgalib} \
%endif
		`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

install lib/{gs_frsd,pdfopt,pdfwrite}.ps $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc \
	$RPM_BUILD_ROOT%{_bindir}/*.sh \
	$RPM_BUILD_ROOT%{_mandir}/man1/{ps2pdf1{2,3},gsbj,gsdj,gsdj500,gslj}.1

echo ".so gs.1"     > $RPM_BUILD_ROOT%{_mandir}/man1/ghostscript.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf12.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf13.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsbj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj500.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gslj.1

ln -sf gs $RPM_BUILD_ROOT%{_bindir}/ghostscript

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.htm
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lib
# "*.*" will not match "Fontmap". It is OK.
%{_datadir}/%{name}/lib/*.*
%dir %{_datadir}/%{name}/examples
%{_datadir}/%{name}/examples/*
%config %verify(not size md5 mtime) %{_datadir}/%{name}/lib/Fontmap
%{_mandir}/man*/*
